from django.db import models
from django.utils.translation import gettext_lazy as _
class Sexe(models.TextChoices):
    MASCULIN = "M", "Masculin"
    FEMININ = "F", "Féminin"


class Quarter(models.Model):
    name_quart = models.CharField(max_length=100, verbose_name=_("nom du quartier"))
    district_quart = models.CharField(max_length=100, verbose_name=_("commune du quartier"))

    class Meta:
        db_table = "Quarter"
        verbose_name= _("Quartier")
        verbose_name_plural =_("Quartiers")

    def __str__(self):
        return f"{self.name_quart} ({self.district_quart})"


class Commissioner(models.Model):

    """le modele commissionnaire qui gere les donnees du commissionnaire depuis leurs bureau"""

    lastname_com = models.CharField(max_length=100, verbose_name=_("nom du commissinnaire"))
    firstname_com = models.CharField(max_length=100, verbose_name=_("prenom du commissionnaire"))
    sex_com = models.CharField(max_length=1, choices=Sexe.choices, verbose_name=_("sexe du commissionaire"))
    adress_com = models.CharField(max_length=255, verbose_name=_("adresse du commissionnaire"))
    register = models.CharField(max_length=100, unique=True, verbose_name=_("matricule du commissionnaire"))
    nationality_com = models.CharField(max_length=100, verbose_name=_("nationnlite du commissionnaire"))
    number_com = models.CharField(max_length=20, verbose_name=_("numero du commissionnaire"))
    email_com = models.EmailField(unique=True, verbose_name=_("email du commissionnaire"))
    profil_com = models.ImageField (upload_to="commissionnaire_profiles/", null=True, blank=True, verbose_name=_("profile du commissionnaire"))

    class Meta:
        db_table = "commissioner"
        verbose_name = _("Commissionnaire")
        verbose_name_plural = _("Commissionnaires")
        ordering=["lastname_com","firstname_com"]

    def __str__(self):
        return f"{self.lastname_com_com} {self.firstname_com}"

class User_com(models.Model):

    """le modele user commissionnaire qui gere les donnees du commissionnaire qui se s'inscrit dans l'application"""

    lastname_user_com = models.CharField (max_length=100, verbose_name=_("nom commissionaire inscrit"))
    firstname_user_com = models.CharField(max_length=100, verbose_name=_("prenom commissionnaire inscrit"))
    register_user_com = models.CharField(max_length=100, unique=True, verbose_name=_("matricule commissionnaire inscrit"))
    sex_user_com = models.CharField(max_length=1, choices=Sexe.choices, verbose_name=_("sexe commissionnaire inscrit"))
    email_user_com = models.EmailField(unique=True, verbose_name=_("email commissionnaire inscrit"))
    number_user_com = models.CharField(max_length=20, verbose_name=_("numero du commissionnaire inscrit"))
    password_user_com = models.CharField(max_length=50, verbose_name=_("mot de passe du commaissionnaire inscrit"))

    class Meta:
        db_table = "user_com"
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")
        ordering=["lastname_user_com","firstname_user_com"]

    def __str__(self):
        return f"{self.lastname_user_com} - {self.firstname_user_com}"


class House(models.Model):

    """le modele maison qui gere les donnees de la maison publiee"""

    profil_house = models.ImageField(verbose_name=_("profile de la maison"))
    piece_house = models.PositiveIntegerField(verbose_name=_("pièce de la maison"))
    description = models.TextField(verbose_name=_("description de la maison"))
    quarter = models.ForeignKey(
        Quarter, on_delete=models.PROTECT, related_name="maisons", verbose_name=_("quartier de la maion")
    )
    rent = models.DecimalField(max_digits=12, decimal_places=2,verbose_name=_("loyer de la maison"))
    bail = models.DecimalField(max_digits=12, decimal_places=2,verbose_name=_("garantie de la maison"))
    user_com_id= models.ForeignKey(
        User_com, on_delete=models.CASCADE, related_name="maisons", verbose_name=_("commissionnaire de la maison")
    )

    class Meta:
        db_table = "house"
        verbose_name = "Maison"
        verbose_name_plural = "Maisons"

    def __str__(self):
        return f"House {self.quarter}"

class PictureHouse(models.Model):

    """le modele photo maison qui gere les photos de la maison publiee"""

    img_house = models.ImageField(upload_to="photos/", null=True, blank=True)
    id_house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True,blank=True, related_name= 'photo_maisons')

    class Meta:
        db_table = "picture_house"
        verbose_name = "Photo_maison"
        verbose_name_plural = "Photo_maisons"

    def __str__(self):
        return f"PictureHouse {self.id_photo} - House {self.maison_id}"
    
class DataLocation(models.Model):

    """donnees pour la demande de location """

    class StateCivil(models.TextChoices):

        """Le choix d'etat civil pour le locataire"""

        UNMARRIED = "Célibataire"
        MARRIED = "Marié(e)"
        

    lastname_loc = models.CharField(max_length=100, verbose_name=_("nom du locataire"))
    firstname_loc = models.CharField(max_length=100, verbose_name=_("prenom du locataire"))
    number_loc = models.CharField(max_length=20, verbose_name=_("numero du locataire"))
    email_loc = models.EmailField(verbose_name=_("email du locataire"))
    statecivil_loc = models.CharField(max_length=20, choices=StateCivil.choices, verbose_name=_("etat civil du locataire"))
    child_loc = models.PositiveIntegerField(default=0, verbose_name=_("enfant locataire"))
    sex_loc = models.CharField(max_length=1, choices=Sexe.choices, verbose_name=_("sexe du locataire"))
    adress_loc = models.CharField(max_length=255, verbose_name=_("adresse du locataire"))
    nationality_loc = models.CharField(max_length=100, verbose_name=_("nationnalite du locataire"))
    maison = models.ForeignKey(
        House,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="locations",
        verbose_name=_("maison choisie")
    )

    class Meta:
        db_table = "data_location"
        verbose_name = "Demande"
        verbose_name_plural = "Demandes"

    def __str__(self):
        return f"{self.lastname_loc} - {self.firstname_loc}"


class Administration(models.Model):

    """le modele administration qui gere les donnees(statistiques) de l'application"""

    user_com_id= models.ForeignKey(User_com, on_delete=models.CASCADE, related_name="administration", verbose_name=_("commissionnaires inscrits"))
    data_id = models.ForeignKey(DataLocation, on_delete=models.CASCADE, related_name="administration", verbose_name=_("demande envoyer"))

    class Meta:
        db_table = "administration"
        verbose_name ="Administration"
        verbose_name_plural ="Administrations"


class Auth_admin(models.Model):

    email_auth = models.EmailField(unique=True, verbose_name=_("email de l'admin"))
    password_auth = models.CharField(max_length=100, verbose_name=_("password de l'admin"))

    def __str__(self):
        return f"{self.email_auth}"

    class Meta:
        db_table="auth_admin"
        verbose_name =_("Authentification")
        verbose_name_plural =_("Authentifications")