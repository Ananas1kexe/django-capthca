from django.shortcuts import render
import secrets
import string
import io
import time
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.urls import reverse
# Create your views here.
def main(request):
    return render(request, "capthca.html", {
        "next": reverse("index"),
        "now": timezone.now(),
    })
def index(reuqest):
    return render(reuqest, "index.html")


def _generate_code(length=5):
    alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase
    return "".join(secrets.choice(alphabet) for _ in range(length))

def captcha_image(reuqest):
    code = _generate_code()
    reuqest.session["captcha_code"] = code
    
    img = Image.new("RGB", (120, 40), color=(255,255,255))
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.load_default()
    
    for i in range(8):
        draw.line([
            (randint(0, 120), randint(0, 40)),
            (randint(0, 120), randint(0, 40))],
                randint(0, 255), 2)
        
    bbox = draw.textbbox((0,0), code, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((120-w)/2, (40-h)/2), code, font=font, fill=(0,0,0))
    
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return HttpResponse(buf.read(), content_type="image/png")

@require_http_methods(["GET", "POST"])
def captcha_verify(request):
    data = request.POST if request.method == "POST" else request.GET
    user_input = data.get("captcha", "").strip()
    next_url = data.get("next", "") or reverse("index")  

    if not next_url or next_url == "None":
        next_url = reverse("index")

    real_code = request.session.get("captcha_code", "")

    if user_input and real_code and user_input == real_code:
        request.session["passed_captcha"] = True
        request.session.pop("captcha_render_time", None)
        return HttpResponseRedirect(next_url) 
    else:
        request.session["captcha_render_time"] = time.time()
        return render(
            request,
            "capthca.html",
            {
                "error": "Wrong code, try again",
                "next": next_url, 
                "now": timezone.now(),
            },
        )

@require_http_methods(["GET", "POST"])
def capthca(request):
    if not request.session.get("passed_captcha"):
        return render(
            request,
            "capthca.html",
            {
                "error": "Wrong code, try again",
                "now": timezone.now(),
            },
        )
    next_url = request.GET.get("next")
    request.session.pop("passed_captcha", None)
    return HttpResponseRedirect(next_url)