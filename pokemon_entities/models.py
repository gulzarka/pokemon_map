from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('имя', max_length=200)
    title_en = models.CharField(
        "англ.имя", max_length=200, blank=True
        )
    title_jp = models.CharField(
        "яп.имя", max_length=200, blank=True
        )
    image = models.ImageField(
        'картинка', blank=True, null=True)
    description = models.TextField("описание", blank=True)
    previous_evolution = models.ForeignKey(
        'self', blank=True, null=True,
        related_name='next_evolutions',
        on_delete=models.SET_NULL,
        verbose_name='Из кого эволюционировал'
        )

    def __str__(self) -> str:
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        verbose_name='покемон',
        related_name='pokemon_entities'
        )
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField("время появления", null=True)
    disappeared_at = models.DateTimeField("время исчезновения", null=True)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon}'
