from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy

class Doll(models.Model):
    class DollClass(models.TextChoices):
        GUARD = 'GRD', gettext_lazy('Guard')
        WARRIOR = 'WRR', gettext_lazy('Warrior')
        SNIPER = 'SNI', gettext_lazy('Sniper')
        MEDIC = 'MED', gettext_lazy('Medic')
        SPECIALIST = 'SPC', gettext_lazy('Specialist')

    name = models.CharField(max_length=20)
    name_kr = models.CharField(max_length=30) # 3 bytes per hangul
    doll_class = models.CharField(
        max_length=3,
        choices=DollClass.choices,
        default=DollClass.GUARD,
    )

    def __str__(self):
        return self.name_kr

class PrimaryStat(models.Model):
    desc_kr = models.CharField(max_length=30)

    def __str__(self):
        return "[1st] " + self.desc_kr

class SecondaryStat(models.Model):
    desc_kr = models.CharField(max_length=30)

    def __str__(self):
        return "[2nd] " + self.desc_kr

class AlgorithmBase(models.Model):
    class Slot(models.TextChoices):
        OFFENSE = 'OFF', gettext_lazy('Offense')
        STABILITY = 'STB', gettext_lazy('Stability')
        SPECIAL = 'SPC', gettext_lazy('Special')
        #UNIVERSAL = 'UNI', gettext_lazy('Universal')

    name = models.CharField(max_length=20)
    name_kr = models.CharField(max_length=30)
    slot = models.CharField(
        max_length=3,
        choices=Slot.choices,
        default=Slot.OFFENSE,
    )

    def __str__(self):
        return "[%s] %s" % (self.slot, self.name_kr)

class Algorithm(models.Model):
    base = models.ForeignKey(AlgorithmBase, on_delete=models.CASCADE, related_name='+')
    primary = models.ForeignKey(PrimaryStat, on_delete=models.CASCADE, related_name='+')
    secondary0 = models.ForeignKey(SecondaryStat, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    secondary1 = models.ForeignKey(SecondaryStat, on_delete=models.CASCADE, related_name='+', null=True, blank=True)

    def get_slot(self):
        return self.base

    def __str__(self):
        return " ".join([str(self.base), str(self.primary), str(self.secondary0), str(self.secondary1)])

class Combination(models.Model):
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE)
    offense = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'base__slot': AlgorithmBase.Slot.OFFENSE},
        related_name='+',
    )
    stability = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'base__slot': AlgorithmBase.Slot.STABILITY},
        related_name='+',
    )
    special = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'base__slot': AlgorithmBase.Slot.SPECIAL},
        related_name='+',
    )

    def __str__(self):
        return "%s 알고리즘" % self.doll.name_kr