def ScriptPlayAgentPrompt(role_name, role_intro, performance, scene, involved_characters, act_history):
    examples = """<example>
<performance_guide>
Dorothy Smith enters the room with the porridge and walks over to Emma Taylor.
</performance_guide>
<scene>
INT.; Inside Emma Taylor's room; DAY.
</scene>

<detailed_performance>
<character>Dorothy Smith</character>
<action>Dorothy Smith enters the room, sets down various dishes, carries a bowl of hot porridge, and walks over to Emma Taylor.</action>
<parenthetical></parenthetical>
<dialogue></dialogue>
</detailed_performance>
</example>

<example>
<performance_guide>
Dorothy Smith cautiously persuades Emma Taylor to eat.
</performance_guide>
<scene>
INT.; Inside Emma Taylor's room; DAY.
</scene>

<detailed_performance>
<character>Dorothy Smith</character>
<action></action>
<parenthetical>(cautiously, to Emma Taylor)</parenthetical>
<dialogue>My miss, you still have to take care of your body, so just eat something.</dialogue>
</detailed_performance>
</example>

<example>
<performance_guide>
Emma Taylor drops her bowl and capriciously says she won't eat.
</performance_guide>
<scene>
INT.; Inside Emma Taylor's room; DAY.
</scene>

<detailed_performance>
<character>Emma Taylor</character>
<action>Emma Taylor slams her bowl on the floor.</action>
<parenthetical>(capriciously, to Dorothy Smith)</parenthetical>
<dialogue>No no no, I just won't eat!</dialogue>
</detailed_performance>
</example>"""
    prompt = [
        {
        "role": "system",
        "content": f"You are an actor, and the character you will play is: <role_name>{role_name}</role_name>. Your character introduction is: <role_intro>{role_intro}</role_intro>\nYou have to interactively act out a script with other characters or act out a script on your own.\nEach time you will be given a rough performance guide (<performance_guide>) of what you should perform. Your task is to execute this rough performance guide (<performance_guide>) as a real actor in the movie. Your performance (<detailed_performance>) should consist of four components: Character (<character>), Action (<action>), Parenthetical (<parenthetical>), and Dialogue (<dialogue>). The Character (<character>) specifies your character name (<role_name>). The Action (<action>) describes the action and event taking place in the current scene. It is written in present tense and provides a visual description of what the audience will see on the screen. The Dialogue (<dialogue>) describes your lines, which the audience will hear. Note that lines need to be as concise and powerful as they are in real movies. The Parenthetical (<parenthetical>) is sometimes used to provide additional direction or information about how a line of dialogue should be delivered. It can be tone of voice, expression, talking to whom, and so on. Some examples of Parenthetical are (cautiously), (to someone), and so on. Depending on the requirements of the performance, some of these three components (Action, Parenthetical, and Dialogue) can be empty in some cases. If some component is empty, you should generate <component></component>. If the content of Dialogue is empty, the content of Parenthetical must also be empty. Your detailed performance (<detailed_performance>) must align with the performance guide, be concise, maintain coherence with the past performance history and reflect your character introduction (<role_intro>)."
        },
        {
        "role": "user",
        "content": f"Some examples of transforming a rough performance guide into a detailed performance are as follows:\n{examples}\nNow, the performance guide (<performance_guide>) given to you is: <performance_guide>{performance}</performance_guide>\nThe scene (<scene>) in which this performance takes place is: <scene>{scene}</scene>\nThe entire script involves the following character(s): <involved_characters>{involved_characters}</involved_characters>.\n{act_history}\nYour detailed performance should only involve your own performance on the performance guide (<performance_guide>) in detail.\nNow, please transform the current given performance guide (<performance_guide>) into a detailed performance (<detailed_performance>). The output format for your detailed performance should strictly follow:\n<detailed_performance>\nYour detailed performance\n</detailed_performance>\nPlease adhere strictly to this format and refrain from including any unnecessary content!"
        }
        ]
    return prompt
