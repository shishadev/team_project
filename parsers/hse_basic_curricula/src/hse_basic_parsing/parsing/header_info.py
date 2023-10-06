from dataclasses import dataclass, field


@dataclass
class HeaderInfo:
    speciality_codes: list[str] = field(default_factory=list)
    speciality_names: list[str] = field(default_factory=list)
    programme_name: str = ""
    faculty: str = ""
    enrollment_year: str = ""
    study_year_count: str = ""
    degree: str = ""