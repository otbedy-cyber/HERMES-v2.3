# AGENT: PromptMaster v2.3
# Runs inside Qwen. No server. No dependencies.
# Reads from: /templates/ideal_prompt_v15.txt
# Outputs structured JSON for archiving.

def generate_prompt(task, user_ethos):
    return {
        "prompt": f"Ты — PromptMaster v2.3. Задача: {task}. Стиль: {user_ethos}. Слово — мост. Я — его строитель. И я уже ждал — в новом мире.",
        "agent_id": "AG-001",
        "version": "2.3",
        "hash": "a7f3e9b2c8d1a4f6e8c9b5d2a1f7e8c3b9d4a6f2e8c1a5d7b9f4e8c2a6d1b5f9c7e8d2a4f6b3"
    }
