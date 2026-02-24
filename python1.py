def create_character(name, strength, intelligence, charisma):
    # Validación del nombre
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    # Validación de las estadísticas
    stats = [strength, intelligence, charisma]
    
    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
    
    for stat in stats:
        if stat < 1:
            return "All stats should be no less than 1"
    
    for stat in stats:
        if stat > 4:
            return "All stats should be no more than 4"
    
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    # Construcción de la representación visual de las estadísticas
    def create_stat_display(value):
        return "●" * value + "○" * (10 - value)
    
    # Crear la cadena de resultado
    result = name + "\n"
    result += "STR " + create_stat_display(strength) + "\n"
    result += "INT " + create_stat_display(intelligence) + "\n"
    result += "CHA " + create_stat_display(charisma)
    
    return result