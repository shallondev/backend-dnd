
from django.shortcuts import render
from .forms import CharacterForm, AbilityScoreForm, SkillForm, EquipmentForm
from .models import Character, AbilityScore, Skill, Equipment

def character_sheet(request):
    character_form = CharacterForm()
    ability_score_form = AbilityScoreForm()
    skill_form = SkillForm()
    equipment_form = EquipmentForm()
    
    characters = Character.objects.all()
    ability_scores = AbilityScore.objects.all()
    skills = Skill.objects.all()
    equipment = Equipment.objects.all()
    
    context = {
        'character_form': character_form,
        'ability_score_form': ability_score_form,
        'skill_form': skill_form,
        'equipment_form': equipment_form,
        'characters': characters,
        'ability_scores': ability_scores,
        'skills': skills,
        'equipment': equipment,
    }
    return render(request, 'crud/character_sheet.html', context)
