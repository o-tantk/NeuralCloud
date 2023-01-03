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

class Algorithm(models.Model):
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
    is_useless = models.BooleanField(default=False)

    def icon(self):
        return self.name_kr.replace(' ', '_')

    def __str__(self):
        return "[%s] %s" % (self.slot, self.name_kr)

class Stat(models.Model):
    name_kr = models.CharField(max_length=50)
    alias_kr = models.CharField(max_length=30)

    def __str__(self):
        return self.name_kr

    class Meta:
        ordering = ['name_kr']

class RecommendedSet(models.Model):
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE)
    offense_algorithm = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'slot': Algorithm.Slot.OFFENSE},
        related_name='+',
    )
    offense_primary_stats = models.ManyToManyField(Stat, related_name='+')
    offense_primary_stat_kr = models.CharField(max_length=50)
    offense_secondary_stat_kr = models.CharField(max_length=50, blank=True)

    stability_algorithm = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'slot': Algorithm.Slot.STABILITY},
        related_name='+',
    )
    stability_primary_stats = models.ManyToManyField(Stat, related_name='+')
    stability_primary_stat_kr = models.CharField(max_length=50)
    stability_secondary_stat_kr = models.CharField(max_length=50, blank=True)

    special_algorithm = models.ForeignKey(
        Algorithm,
        on_delete=models.CASCADE,
        limit_choices_to={'slot': Algorithm.Slot.SPECIAL},
        related_name='+',
    )
    special_primary_stats = models.ManyToManyField(Stat, related_name='+')
    special_primary_stat_kr = models.CharField(max_length=50)
    special_secondary_stat_kr = models.CharField(max_length=50, blank=True)

    def algorithm_list(self):
        return [
            {'algorithm': self.offense_algorithm, 'primary': self.offense_primary_stats.all()},
            {'algorithm': self.stability_algorithm, 'primary': self.stability_primary_stats.all()},
            {'algorithm': self.special_algorithm, 'primary': self.special_primary_stats.all()},
        ]

    def __str__(self):
        return "%s 알고리즘" % self.doll.name_kr
