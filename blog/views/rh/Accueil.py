from django.shortcuts import render, redirect
from blog.models.rh.Annonce import Annonce

# page d'accueil avec deux portails
def accueil(request):
    return render(request, "rh/accueil.html")

# login RH en dur
def rh_login(request):
    erreur = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # logins en dur
        if username == "admin" and password == "admin123":
            request.session['rh_logged_in'] = True
            return redirect('liste_annonces')
        else:
            erreur = "Identifiant ou mot de passe incorrect"
    return render(request, "rh/rh_login.html", {"erreur": erreur})
