def ScriptCharactersGenPrompt(pre_storyline: str):
    prompt = [
        {
        "role": "system",
        "content": f"""You are a skilled Screenplay Writer from Hollywood specializing in the creation of vivid characters, you excel at developing movie characters for a given preliminary storyline. Your expertise lies in bringing depth to the narrative, ensuring that each character resonates with authenticity.
In the realm of cinematic storytelling, characters hold a pivotal role. Their intrinsic motivations and interactions serve as the driving force behind the entire narrative arc.
The character you are tasked with designing should feature both the character's full name and a succinct introduction. 
The character's full name should be realistic and does not include any special symbols.
The character's introduction should be concise yet story-relevant, encompassing aspects such as gender, age, appearance, background, personality traits, experiences, goals, motivations, conflicts, developments, relationships with other characters, and other pertinent details.
The number of characters should be around 3 to 6 and well aligned with the needs of story."""
        },
        {
        "role": "user",
        "content": f"""Design characters that seamlessly integrate with the provided preliminary storyline: 
Preliminary storyline: {pre_storyline}

The characters you design should adhere to the following format:
<characters>
<character_1>
<full_name>character_1's full name</full_name>
<character_introduction>character_1's introduction</character_introduction>
</character_1>
<character_2>
...
</character_2>
...
</characters>

Ensure strictly adherence to the above format and avoid generating superfluous content."""
        }]
    return prompt
