from AGENTS.blueprint_architect_agent import run as a
from AGENTS.item_writer_agent import run as b
from AGENTS.difficulty_calibrator_agent import run as c
from AGENTS.rubric_designer_agent import run as d
from AGENTS.assessment_auditor_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
