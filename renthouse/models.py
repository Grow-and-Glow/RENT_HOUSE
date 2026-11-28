from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Sexe(models.TextChoices):
    MASCULIN = "M", "Masculin"
    FEMININ = "F", "Féminin"


class TransactionType(models.TextChoices):
    LOCATION = "LOCATION", "À louer"
    VENTE = "VENTE", "À vendre"

class HouseType(models.TextChoices):
    MAISON = "MAISON", "Maison"
    APPARTEMENT = "APPARTEMENT", "Appartement"
    VILLA = "VILLA", "Villa"

class HouseStatus(models.TextChoices):
    PENDING = "EN_ATTENTE", "En attente"
    PUBLISHED = "PUBLIEE", "Publiée"
    REFUSED = "REFUSEE", "Refusée"


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
        return f"{self.lastname_com} {self.firstname_com}"

class UserCom(models.Model):

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
    title = models.CharField(max_length=150, default="Maison", verbose_name=_("titre"))
    house_type = models.CharField(max_length=20, choices=HouseType.choices, default=HouseType.MAISON)
    transaction_type = models.CharField(max_length=10, choices=TransactionType.choices, default=TransactionType.LOCATION)
    status = models.CharField(max_length=12, choices=HouseStatus.choices, default=HouseStatus.PENDING)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    profil_house = models.ImageField(upload_to="houses/profiles/", verbose_name=_("profile de la maison"))
    rent = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=_("loyer de la maison"))
    bail = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=_("garantie de la maison"))
    sale_price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True, verbose_name=_("prix de vente"))
    created_at = models.DateTimeField(default=timezone.now)
    piece_house = models.PositiveIntegerField(verbose_name=_("pièce de la maison"))
    description = models.TextField(verbose_name=_("description de la maison"))
    quarter = models.ForeignKey(
        Quarter, on_delete=models.PROTECT, related_name="maisons", verbose_name=_("quartier de la maion")
    )
    user_com_id= models.ForeignKey(
        UserCom, on_delete=models.CASCADE, related_name="maisons", verbose_name=_("commissionnaire de la maison")
    )

    @property
    def is_rental(self):
        return self.transaction_type == TransactionType.LOCATION

    @property
    def price(self):
        return self.rent if self.is_rental else self.sale_price

    class Meta:
        db_table = "house"
        verbose_name = "Maison"
        verbose_name_plural = "Maisons"
        ordering = ["-created_at"]

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
        return f"PictureHouse {self.pk} - House {self.id_house_id}"
    
class DataLocation(models.Model):

    """donnees pour la demande de location """

    class StateCivil(models.TextChoices):

        """Le choix d'etat civil pour le locataire"""

        UNMARRIED = "Célibataire"
        MARRIED = "Marié(e)"
        

    lastname_loc = models.CharField(blank=True, null=True, max_length=100, verbose_name=_("nom du locataire"))
    firstname_loc = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("prenom du locataire"))
    number_loc = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("numero du locataire"))
    email_loc = models.EmailField(verbose_name=_("email du locataire"))
    statecivil_loc = models.CharField(max_length=20, blank=True, null=True, choices=StateCivil.choices, verbose_name=_("etat civil du locataire"))
    child_loc = models.PositiveIntegerField(default=0, verbose_name=_("enfant locataire"))
    sex_loc = models.CharField(max_length=1, blank=True, null=True, choices=Sexe.choices, verbose_name=_("sexe du locataire"))
    adress_loc = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("adresse du locataire"))
    nationality_loc = models.CharField(blank=True, null=True, max_length=100, verbose_name=_("nationnalite du locataire"))
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

    user_com_id= models.ForeignKey(UserCom, on_delete=models.CASCADE, related_name="administration", verbose_name=_("commissionnaires inscrits"))
    data_id = models.ForeignKey(DataLocation, on_delete=models.CASCADE, related_name="administration", verbose_name=_("demande envoyer"))

    class Meta:
        db_table = "administration"
        verbose_name ="Administration"
        verbose_name_plural ="Administrations"
