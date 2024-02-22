SELECT_ALL = "SELECT character_id, name FROM charactercreator_character;"

AVG_ITEM_WEIGHT_PER_CHARACTER = """
    SELECT cc_char.name, AVG(ai.weight) FROM charactercreator_character as cc_char
    JOIN charactercreator_character_inventory as cc_inv
    ON	cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id
    """
