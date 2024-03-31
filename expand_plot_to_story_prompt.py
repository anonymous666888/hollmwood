def ScriptOutlineExpandPrompt(plot, pre_storyline, scene, characters, previous_stroy_content, last_plot: bool):
    if last_plot is True:
        last_plot_str = "The current story plot point you need to expand is the last plot point of the story. So, make sure that your expanded story chapter has a clear end to the story."
    else:
        last_plot_str = ""  
    prompt = [
        {
        "role": "system",
        "content": f"""You are a writer, your task is to expand upon one of the story plot points in an existing story outline, transforming it into a complete story chapter while maintaining coherence and consistency with the previous happened story content. The story needs to be specific, with dramatic conflict that captures the audience's attention and resonates with them."""
        },
        {
        "role": "user",
        "content": f"""The current story plot point you need to expand is:\n<plot_point>{plot}</plot_point>\nThe storyline is:\n<storyline>\n{pre_storyline}\n</storyline>\nThe scene where the current story plot point happens is: <scene>{scene}</scene>\n{characters}\n{previous_stroy_content}\n{last_plot_str}\nNow, please expand the current given story plot point (<plot_point>) in a story outline into a chapter of complete story content which keeps coherent with the previous happened story content. Feel free to add details around the plot point but avoid deviating too far from it. While you have the flexibility to introduce additional details surrounding the plot point, it is essential to stay aligned with the original plot point's core content. To maintain conciseness, the expanded word count should be as minimal as possible, effectively unfolding the plot point while creating a complete story chapter.\nYour output format for the expanded story content should strictly follow: \n<chapter>\nThe story chapter you have expanded\n</chapter>\nPlease adhere strictly to this format and refrain from including any unnecessary content!"""
        }]
    return prompt

