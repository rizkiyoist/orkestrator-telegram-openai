# modifikasi dari https://github.com/openai/openai-python originally licensed under Apache-2.0
#
# Copyright (c) Rizki Hadiaturrasyid
#

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="Anda adalah asisten Orkestrator AI",
    input="Bagaimana cara mengubah int ke str?",
)

print(response.output_text)