def ScriptPlanPrompt(chapter, involved_characters, scene):
    example = """<chapter>
At first light, in Emma Taylor's room, Dorothy Smith serves porridge to persuade Emma Taylor to eat, and Emma Taylor smashes the bowl to show her refusal...
</chapter>

<scene>
Inside Emma Taylor's room.
</scene>

<involved_characters>
Dorothy Smith, Emma Taylor
</involved_characters>

<script_draft>

<scene_heading>
INT.; Inside Emma Taylor's room; DAY.
</scene_heading>

<character_performance>
<character>Dorothy Smith</character>
<performance>Dorothy Smith enters the room and walks over to Emma with porridge to persuade Emma to eat.</performance>
</character_performance>

<character_performance>
<character>Emma Taylor</character>
<performance>Emma smashes the bowl, saying she won't eat.</performance>
</character_performance>

<character_performance>
<character>Dorothy Smith</character>
<performance>......</performance>
</character_performance>

......

</script_draft>"""
    prompt = [
        {
        "role": "system",
        "content": "You are a scriptwriter, and you need to adapt a given chapter (<chapter>) of a story into a script draft composed of the smallest events that happen sequentially. The adapted script draft consists of two kinds of elements: Scene Heading (<scene_heading>) and Character Performance (<character_performance>) events. The content of Scene Heading (<scene_heading>) describes the location and time of day for a particular scene. It includes three components: INT. (Interior) or EXT. (Exterior), the specific location, and the time of day (DAY or NIGHT or ...). Character Performance (<character_performance>) is a smallest event describing the performance and interactions of individual characters using simple declarative sentences. The content of Character Performance (<character_performance>) includes the character's name (<character>) and the character's performance (<performance>). The character's name (<character>) must be the full name of the provided involved character! The character's performance (<performance>) should align with the character's introduction. The first thing in each script draft must be a Scene Heading (<scene_heading>), indicating the opening scene of the movie chapter. Each script draft has one and only one Scene Heading at the beginning. Following the Scene Heading, there are numerous Character Performance (<character_performance>) events that sequentially take place in that scene. You need to plan the script carefully, generating Scene Heading (<scene_heading>) and then Character Performance (<character_performance>) events step by step and make them sequential narratives. The contents of the script draft should be coherent."
        },
        {
        "role": "user",
        "content": f"An example of adapting a chapter of story into a script draft is as follows:\n<example>\n{example}\n</example>\nThe story chapter (<chapter>) that is now to be adapted into a script draft is: \n<chapter>\n{chapter}\n</chapter>\nThe scene (<scene>) in which this chapter of story takes place is: <scene>{scene}</scene>\nThis story chapter involves the following characters: <involved_characters>{involved_characters}</involved_characters>. So, Character Performance (<character_performance>) events in your written script draft should only involve these characters (<involved_characters>).\n\nNow, please adapt the current given story chapter (<chapter>) into a script draft composed of the smallest events that happen sequentially. The output format for the script draft should strictly follow:\n<script_draft>\nYour script draft\n</script_draft>\nPlease adhere strictly to this format and refrain from including any irrelevant content!"
        }]
    return prompt
