import re
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from skills.models import Category, Skill


class Command(BaseCommand):
    help = "Charge les catégories et compétences depuis le fichier CCTP."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(settings.BASE_DIR / "CCTP" / "CCTP.md"),
            help="Chemin vers le fichier CCTP.md",
        )
        parser.add_argument(
            "--purge",
            action="store_true",
            help="Supprime les compétences existantes avant rechargement",
        )

    def handle(self, *args, **options):
        path = Path(options["file"])
        if not path.exists():
            self.stderr.write(self.style.ERROR(f"Fichier introuvable : {path}"))
            return

        content = path.read_text(encoding="utf-8")

        sections = self._parse(content)

        if options["purge"]:
            deleted = Skill.objects.all().delete()[0]
            self.stdout.write(f"{deleted} compétence(s) supprimée(s).")

        created_categories = 0
        created_skills = 0

        for category_name, skills in sections.items():
            category, created = Category.objects.get_or_create(
                name=category_name, defaults={"slug": slugify(category_name)}
            )
            if created:
                created_categories += 1

            for skill_name in skills:
                _, created = Skill.objects.get_or_create(
                    name=skill_name, category=category
                )
                if created:
                    created_skills += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed terminé : {created_categories} catégorie(s) et "
                f"{created_skills} compétence(s) créées "
                f"({len(sections)} catégories traitées)."
            )
        )

    def _parse(self, content):
        """Retourne {nom_catégorie: [compétences]} depuis le markdown."""
        result = {}
        current = None
        in_skills_section = False

        for line in content.splitlines():
            if line.startswith("## Compétences par catégories"):
                in_skills_section = True
                continue
            if not in_skills_section:
                continue

            match = re.match(r"^###\s+(.+)$", line)
            if match:
                current = match.group(1).strip()
                result.setdefault(current, [])
                continue

            if current is not None and line.startswith("- "):
                skill = line[2:].strip()
                if skill:
                    result[current].append(skill)

        return result
