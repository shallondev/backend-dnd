from django import forms
from .models import Character, AbilityScore, Skill, Equipment

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'character_class', 'level', 'background', 'alignment', 'experience_points']

class AbilityScoreForm(forms.ModelForm):
    class Meta:
        model = AbilityScore
        fields = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency', 'modifier']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'quantity']
