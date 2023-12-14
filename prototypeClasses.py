def prototype_subclass(cls):
    cls._instances = {}  # Class-level dictionary to store instances

    def get_instance(cls, name):
        # Retrieve an instance by name
        return cls._instances.get(name)

    def get_all_instances(cls):
        # Get a dictionary of all instances, with names as keys
        return cls._instances

    cls.get_instance = classmethod(get_instance)
    cls.get_all_instances = classmethod(get_all_instances)

    # Override the original __init__ method to store instances
    original_init = cls.__init__

    def new_init(self, name, type, *args, **kwargs):
        original_init(self, name, type, *args, **kwargs)
        cls._instances[name] = self

    cls.__init__ = new_init
    return cls


class PrototypeBase:
    _instances = {}  # Class-level dictionary to store instances

    def __init__(self, name, type, localised_description=None, localised_name=None, order=None):
        self.name = name
        self.type = type
        self.localised_description = localised_description
        self.localised_name = localised_name
        self.order = order
        # Add the instance to the class-level dictionary
        self._instances[name] = self

    @classmethod
    def get_instance(cls, name):
        # Retrieve an instance by name
        return cls._instances.get(name, None)

    @classmethod
    def get_all_instances(cls):
        # Get a dictionary of all instances, with names as keys
        return cls._instances


class Entity(PrototypeBase):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None):
        super().__init__(name, type, localised_description, localised_name, order)
        self.icons = icons
        self.icon = icon
        self.icon_size = icon_size
        self.additional_pastable_entities = additional_pastable_entities
        self.alert_icon_scale = alert_icon_scale
        self.alert_icon_shift = alert_icon_shift
        self.allow_copy_paste = allow_copy_paste
        self.autoplace = autoplace
        self.build_base_evolution_requirement = build_base_evolution_requirement
        self.build_grid_size = build_grid_size
        self.build_sound = build_sound
        self.close_sound = close_sound
        self.collision_box = collision_box
        self.collision_mask = collision_mask
        self.created_effect = created_effect
        self.created_smoke = created_smoke
        self.drawing_box = drawing_box
        self.emissions_per_second = emissions_per_second
        self.enemy_map_color = enemy_map_color
        self.fast_replaceable_group = fast_replaceable_group
        self.flags = flags
        self.friendly_map_color = friendly_map_color
        self.hit_visualization_box = hit_visualization_box
        self.map_color = map_color
        self.map_generator_bounding_box = map_generator_bounding_box
        self.minable = minable
        self.mined_sound = mined_sound
        self.mining_sound = mining_sound
        self.next_upgrade = next_upgrade
        self.open_sound = open_sound
        self.placeable_by = placeable_by
        self.protected_from_tile_building = protected_from_tile_building
        self.radius_visualisation_specification = radius_visualisation_specification
        self.remains_when_mined = remains_when_mined
        self.remove_decoratives = remove_decoratives
        self.rotated_sound = rotated_sound
        self.selectable_in_game = selectable_in_game
        self.selection_box = selection_box
        self.selection_priority = selection_priority
        self.shooting_cursor_size = shooting_cursor_size
        self.sticker_box = sticker_box
        self.subgroup = subgroup
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.trigger_target_mask = trigger_target_mask
        self.vehicle_impact_sound = vehicle_impact_sound
        self.water_reflection = water_reflection
        self.working_sound = working_sound


class EntityWithHealth(Entity):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None, alert_when_damaged=None,
                 attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None, resistances=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order)
        self.alert_when_damaged = alert_when_damaged
        self.attack_reaction = attack_reaction
        self.corpse = corpse
        self.create_ghost_on_death = create_ghost_on_death
        self.damaged_trigger_effect = damaged_trigger_effect
        self.dying_explosion = dying_explosion
        self.dying_trigger_effect = dying_trigger_effect
        self.healing_per_tick = healing_per_tick
        self.hide_resistances = hide_resistances
        self.integration_patch = integration_patch
        self.integration_patch_render_layer = integration_patch_render_layer
        self.loot = loot
        self.max_health = max_health
        self.random_corpse_variation = random_corpse_variation
        self.repair_sound = repair_sound
        self.repair_speed_modifier = repair_speed_modifier
        self.resistances = resistances


class EntityWithOwner(EntityWithHealth):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None, alert_when_damaged=None,
                 attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, allow_run_time_change_of_is_military_target=None, is_military_target=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect,
                         dying_explosion, dying_trigger_effect, healing_per_tick, hide_resistances,
                         integration_patch, integration_patch_render_layer, loot, max_health,
                         random_corpse_variation, repair_sound, repair_speed_modifier, resistances)
        self.allow_run_time_change_of_is_military_target = allow_run_time_change_of_is_military_target
        self.is_military_target = is_military_target


class CraftingMachine(EntityWithOwner):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None, alert_when_damaged=None,
                 attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, allow_run_time_change_of_is_military_target=None, is_military_target=None,
                 crafting_categories=None, crafting_speed=None, energy_source=None, energy_usage=None,
                 allowed_effects=None, always_draw_idle_animation=None, animation=None,
                 base_productivity=None, default_recipe_tint=None, draw_entity_info_icon_background=None,
                 entity_info_icon_shift=None, fluid_boxes=None, idle_animation=None,
                 match_animation_speed_to_activity=None, module_specification=None,
                 return_ingredients_on_change=None, scale_entity_info_icon=None,
                 shift_animation_transition_duration=None, shift_animation_waypoint_stop_duration=None,
                 shift_animation_waypoints=None, show_recipe_icon=None, show_recipe_icon_on_map=None,
                 status_colors=None, working_visualisations=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances, allow_run_time_change_of_is_military_target,
                         is_military_target)
        self.crafting_categories = crafting_categories
        self.crafting_speed = crafting_speed
        self.energy_source = energy_source
        self.energy_usage = energy_usage
        self.allowed_effects = allowed_effects
        self.always_draw_idle_animation = always_draw_idle_animation
        self.animation = animation
        self.base_productivity = base_productivity
        self.default_recipe_tint = default_recipe_tint
        self.draw_entity_info_icon_background = draw_entity_info_icon_background
        self.entity_info_icon_shift = entity_info_icon_shift
        self.fluid_boxes = fluid_boxes
        self.idle_animation = idle_animation
        self.match_animation_speed_to_activity = match_animation_speed_to_activity
        self.module_specification = module_specification
        self.return_ingredients_on_change = return_ingredients_on_change
        self.scale_entity_info_icon = scale_entity_info_icon
        self.shift_animation_transition_duration = shift_animation_transition_duration
        self.shift_animation_waypoint_stop_duration = shift_animation_waypoint_stop_duration
        self.shift_animation_waypoints = shift_animation_waypoints
        self.show_recipe_icon = show_recipe_icon
        self.show_recipe_icon_on_map = show_recipe_icon_on_map
        self.status_colors = status_colors
        self.working_visualisations = working_visualisations


@prototype_subclass
class Fluid(PrototypeBase):
    def __init__(self, name, type, base_color, default_temperature, flow_color, icons, icon, icon_size,
                 emissions_multiplier=None, fuel_value=None, gas_temperature=None, heat_capacity=None,
                 hidden=None, max_temperature=None, subgroup=None, localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, localised_description, localised_name, order)
        self.base_color = base_color
        self.default_temperature = default_temperature
        self.flow_color = flow_color
        self.icons = icons
        self.icon = icon
        self.icon_size = icon_size
        self.emissions_multiplier = emissions_multiplier
        self.fuel_value = fuel_value
        self.gas_temperature = gas_temperature
        self.heat_capacity = heat_capacity
        self.hidden = hidden
        self.max_temperature = max_temperature
        self.subgroup = subgroup


@prototype_subclass
class Item(PrototypeBase):
    def __init__(self, name, type, stack_size, icons=None, icon_size=None, burnt_result=None, close_sound=None,
                 dark_background_icons=None, default_request_amount=None, flags=None, fuel_acceleration_multiplier=None,
                 fuel_category=None, fuel_emissions_multiplier=None, fuel_glow_color=None,
                 fuel_top_speed_multiplier=None, fuel_value=None, open_sound=None, pictures=None,
                 place_as_tile=None, place_result=None, placed_as_equipment_result=None,
                 rocket_launch_product=None, rocket_launch_products=None, subgroup=None, wire_count=None,
                 localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, localised_description, localised_name, order)
        self.icons = icons
        self.icon_size = icon_size
        self.stack_size = stack_size
        self.burnt_result = burnt_result
        self.close_sound = close_sound
        self.dark_background_icons = dark_background_icons
        self.default_request_amount = default_request_amount
        self.flags = flags
        self.fuel_acceleration_multiplier = fuel_acceleration_multiplier
        self.fuel_category = fuel_category
        self.fuel_emissions_multiplier = fuel_emissions_multiplier
        self.fuel_glow_color = fuel_glow_color
        self.fuel_top_speed_multiplier = fuel_top_speed_multiplier
        self.fuel_value = fuel_value
        self.open_sound = open_sound
        self.pictures = pictures
        self.place_as_tile = place_as_tile
        self.place_result = place_result
        self.placed_as_equipment_result = placed_as_equipment_result
        self.rocket_launch_product = rocket_launch_product
        self.rocket_launch_products = rocket_launch_products
        self.subgroup = subgroup
        self.wire_count = wire_count
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe.name)


@prototype_subclass
class Resource(Item):
    def __init__(self, name, type, stack_size, icons=None, icon_size=None, burnt_result=None, close_sound=None,
                 dark_background_icons=None, default_request_amount=None, flags=None, fuel_acceleration_multiplier=None,
                 fuel_category=None, fuel_emissions_multiplier=None, fuel_glow_color=None,
                 fuel_top_speed_multiplier=None, fuel_value=None, open_sound=None, pictures=None,
                 place_as_tile=None, place_result=None, placed_as_equipment_result=None,
                 rocket_launch_product=None, rocket_launch_products=None, subgroup=None, wire_count=None,
                 localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, stack_size, icons, icon_size, burnt_result, close_sound, dark_background_icons,
                         default_request_amount, flags, fuel_acceleration_multiplier, fuel_category,
                         fuel_emissions_multiplier, fuel_glow_color, fuel_top_speed_multiplier, fuel_value,
                         open_sound, pictures, place_as_tile, place_result, placed_as_equipment_result,
                         rocket_launch_product, rocket_launch_products, subgroup, wire_count, localised_description,
                         localised_name, order)

        # Automatically create a recipe with the same name as the resource
        Recipe(name=name, type="recipe", ingredients=None, result=name, result_count=1)


@prototype_subclass
class Recipe(PrototypeBase):
    def __init__(self, name, type, ingredients, allow_as_intermediate=None, allow_decomposition=None,
                 allow_inserter_overload=None, allow_intermediates=None, always_show_made_in=None,
                 always_show_products=None, category=None, crafting_machine_tint=None, emissions_multiplier=None,
                 enabled=None, energy_required=None, expensive=None, hidden=None,
                 hide_from_player_crafting=None, hide_from_stats=None, icons=None, icon=None, icon_size=None,
                 main_product=None, normal=None, overload_multiplier=None, requester_paste_multiplier=None,
                 result=None, result_count=1, results=None, show_amount_in_title=None, subgroup=None,
                 unlock_results=None, localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, localised_description, localised_name, order)
        self.ingredients = ingredients
        self.allow_as_intermediate = allow_as_intermediate
        self.allow_decomposition = allow_decomposition
        self.allow_inserter_overload = allow_inserter_overload
        self.allow_intermediates = allow_intermediates
        self.always_show_made_in = always_show_made_in
        self.always_show_products = always_show_products
        self.category = category
        self.crafting_machine_tint = crafting_machine_tint
        self.emissions_multiplier = emissions_multiplier
        self.enabled = enabled
        self.energy_required = energy_required
        self.expensive = expensive
        self.hidden = hidden
        self.hide_from_player_crafting = hide_from_player_crafting
        self.hide_from_stats = hide_from_stats
        self.icons = icons
        self.icon = icon
        self.icon_size = icon_size
        self.main_product = main_product
        self.normal = normal
        self.overload_multiplier = overload_multiplier
        self.requester_paste_multiplier = requester_paste_multiplier
        self.result = result
        self.result_count = result_count
        self.results = results
        self.show_amount_in_title = show_amount_in_title
        self.subgroup = subgroup
        self.unlock_results = unlock_results

        # Ensure the item associated with the recipe is aware of the recipe
        if self.result:
            item = Item.get_instance(self.result)
            if item and self.name not in item.recipes:
                item.add_recipe(self)
                # item.recipes.append(self.name)


@prototype_subclass
class AssemblingMachine(CraftingMachine):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None, alert_when_damaged=None,
                 attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, allow_run_time_change_of_is_military_target=None, is_military_target=None,
                 crafting_categories=None, crafting_speed=None, energy_source=None, energy_usage=None,
                 allowed_effects=None, always_draw_idle_animation=None, animation=None,
                 base_productivity=None, default_recipe_tint=None, draw_entity_info_icon_background=None,
                 entity_info_icon_shift=None, fluid_boxes=None, idle_animation=None,
                 match_animation_speed_to_activity=None, module_specification=None,
                 return_ingredients_on_change=None, scale_entity_info_icon=None,
                 shift_animation_transition_duration=None, shift_animation_waypoint_stop_duration=None,
                 shift_animation_waypoints=None, show_recipe_icon=None, show_recipe_icon_on_map=None,
                 status_colors=None, working_visualisations=None, fixed_recipe=None, gui_title_key=None,
                 ingredient_count=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances, allow_run_time_change_of_is_military_target,
                         is_military_target, crafting_categories, crafting_speed, energy_source, energy_usage,
                         allowed_effects, always_draw_idle_animation, animation, base_productivity, default_recipe_tint,
                         draw_entity_info_icon_background, entity_info_icon_shift, fluid_boxes, idle_animation,
                         match_animation_speed_to_activity, module_specification, return_ingredients_on_change,
                         scale_entity_info_icon, shift_animation_transition_duration,
                         shift_animation_waypoint_stop_duration,
                         shift_animation_waypoints, show_recipe_icon, show_recipe_icon_on_map, status_colors,
                         working_visualisations)
        self.fixed_recipe = fixed_recipe
        self.gui_title_key = gui_title_key
        self.ingredient_count = ingredient_count


@prototype_subclass
class Furnace(CraftingMachine):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None, water_reflection=None,
                 working_sound=None, localised_description=None, localised_name=None, order=None,
                 alert_when_damaged=None, attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, result_inventory_size=None, source_inventory_size=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances, result_inventory_size, source_inventory_size)


@prototype_subclass
class Inserter(EntityWithOwner):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None,
                 selectable_in_game=None, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None,
                 tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None, water_reflection=None,
                 working_sound=None, localised_description=None, localised_name=None, order=None,
                 alert_when_damaged=None, attack_reaction=None, corpse=None, create_ghost_on_death=None,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None,
                 healing_per_tick=None, hide_resistances=None, integration_patch=None,
                 integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, energy_source=None, extension_speed=None, hand_base_picture=None,
                 hand_base_shadow=None, hand_closed_picture=None, hand_closed_shadow=None,
                 hand_open_picture=None, hand_open_shadow=None, insert_position=None,
                 pickup_position=None, platform_picture=None, rotation_speed=None,
                 allow_burner_leech=None, allow_custom_vectors=None, chases_belt_items=None,
                 circuit_connector_sprites=None, circuit_wire_connection_points=None,
                 circuit_wire_max_distance=None, default_stack_control_input_signal=None,
                 draw_circuit_wires=None, draw_copper_wires=None, draw_held_item=None,
                 draw_inserter_arrow=None, energy_per_movement=None, energy_per_rotation=None,
                 filter_count=None, hand_size=None, stack=None, stack_size_bonus=None,
                 use_easter_egg=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances)
        self.energy_source = energy_source
        self.extension_speed = extension_speed
        self.hand_base_picture = hand_base_picture
        self.hand_base_shadow = hand_base_shadow
        self.hand_closed_picture = hand_closed_picture
        self.hand_closed_shadow = hand_closed_shadow
        self.hand_open_picture = hand_open_picture
        self.hand_open_shadow = hand_open_shadow
        self.insert_position = insert_position
        self.pickup_position = pickup_position
        self.platform_picture = platform_picture
        self.rotation_speed = rotation_speed
        self.allow_burner_leech = allow_burner_leech
        self.allow_custom_vectors = allow_custom_vectors
        self.chases_belt_items = chases_belt_items
        self.circuit_connector_sprites = circuit_connector_sprites
        self.circuit_wire_connection_points = circuit_wire_connection_points
        self.circuit_wire_max_distance = circuit_wire_max_distance
        self.default_stack_control_input_signal = default_stack_control_input_signal
        self.draw_circuit_wires = draw_circuit_wires
        self.draw_copper_wires = draw_copper_wires
        self.draw_held_item = draw_held_item
        self.draw_inserter_arrow = draw_inserter_arrow
        self.energy_per_movement = energy_per_movement
        self.energy_per_rotation = energy_per_rotation
        self.filter_count = filter_count
        self.hand_size = hand_size
        self.stack = stack
        self.stack_size_bonus = stack_size_bonus
        self.use_easter_egg = use_easter_egg


@prototype_subclass
class Lab(EntityWithOwner):
    def __init__(self, name, type, icons, icon, icon_size, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=None,
                 autoplace=None, build_base_evolution_requirement=None, build_grid_size=None,
                 build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None,
                 remains_when_mined=None, remove_decoratives=None, rotated_sound=None, selectable_in_game=None,
                 selection_box=None, selection_priority=None, shooting_cursor_size=None,
                 sticker_box=None, subgroup=None, tile_height=None, tile_width=None, trigger_target_mask=None,
                 vehicle_impact_sound=None, water_reflection=None, working_sound=None, localised_description=None,
                 localised_name=None, order=None, alert_when_damaged=None, attack_reaction=None, corpse=None,
                 create_ghost_on_death=None, damaged_trigger_effect=None, dying_explosion=None,
                 dying_trigger_effect=None, healing_per_tick=None, hide_resistances=None,
                 integration_patch=None, integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None, resistances=None,
                 energy_source=None, energy_usage=None, inputs=None, off_animation=None, on_animation=None,
                 allowed_effects=None, base_productivity=None, entity_info_icon_shift=None, light=None,
                 module_specification=None, researching_speed=None):
        super().__init__(name, type, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace,
                         build_base_evolution_requirement, build_grid_size, build_sound, close_sound,
                         collision_box, collision_mask, created_effect, created_smoke, drawing_box,
                         emissions_per_second, enemy_map_color, fast_replaceable_group, flags,
                         friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by,
                         protected_from_tile_building, radius_visualisation_specification,
                         remains_when_mined, remove_decoratives, rotated_sound, selectable_in_game,
                         selection_box, selection_priority, shooting_cursor_size, sticker_box, subgroup,
                         tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances)
        self.energy_source = energy_source
        self.energy_usage = energy_usage
        self.inputs = inputs
        self.off_animation = off_animation
        self.on_animation = on_animation
        self.allowed_effects = allowed_effects
        self.base_productivity = base_productivity
        self.entity_info_icon_shift = entity_info_icon_shift
        self.light = light
        self.module_specification = module_specification
        self.researching_speed = researching_speed


@prototype_subclass
class ElectricPole(EntityWithOwner):
    def __init__(self, name, type, connection_points, pictures, supply_area_distance, active_picture=None,
                 draw_circuit_wires=False, draw_copper_wires=False, light=None, maximum_wire_distance=None,
                 radius_visualisation_picture=None, track_coverage_during_build_by_moving=False,
                 allow_run_time_change_of_is_military_target=False, is_military_target=False,
                 alert_when_damaged=False, attack_reaction=None, corpse=None, create_ghost_on_death=False,
                 damaged_trigger_effect=None, dying_explosion=None, dying_trigger_effect=None, healing_per_tick=None,
                 hide_resistances=False, integration_patch=None, integration_patch_render_layer=None, loot=None,
                 max_health=None, random_corpse_variation=False, repair_sound=None, repair_speed_modifier=None,
                 resistances=None, icons=None, icon=None, icon_size=None, additional_pastable_entities=None,
                 alert_icon_scale=None, alert_icon_shift=None, allow_copy_paste=False, autoplace=None,
                 build_base_evolution_requirement=None, build_grid_size=None, build_sound=None, close_sound=None,
                 collision_box=None, collision_mask=None, created_effect=None, created_smoke=None, drawing_box=None,
                 emissions_per_second=None, enemy_map_color=None, fast_replaceable_group=None, flags=None,
                 friendly_map_color=None, hit_visualization_box=None, map_color=None,
                 map_generator_bounding_box=None, minable=None, mined_sound=None, mining_sound=None,
                 next_upgrade=None, open_sound=None, placeable_by=None, protected_from_tile_building=False,
                 radius_visualisation_specification=None, remains_when_mined=None, remove_decoratives=None,
                 rotated_sound=None, selectable_in_game=False, selection_box=None, selection_priority=None,
                 shooting_cursor_size=None, sticker_box=None, subgroup=None, tile_height=None, tile_width=None,
                 trigger_target_mask=None, vehicle_impact_sound=None, water_reflection=None, working_sound=None,
                 localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, allow_run_time_change_of_is_military_target, is_military_target, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace, build_base_evolution_requirement,
                         build_grid_size, build_sound, close_sound, collision_box, collision_mask, created_effect,
                         created_smoke, drawing_box, emissions_per_second, enemy_map_color, fast_replaceable_group,
                         flags, friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box, minable,
                         mined_sound, mining_sound, next_upgrade, open_sound, placeable_by, protected_from_tile_building,
                         radius_visualisation_specification, remains_when_mined, remove_decoratives, rotated_sound,
                         selectable_in_game, selection_box, selection_priority, shooting_cursor_size, sticker_box,
                         subgroup, tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order)
        self.connection_points = connection_points
        self.pictures = pictures
        self.supply_area_distance = supply_area_distance
        self.active_picture = active_picture
        self.draw_circuit_wires = draw_circuit_wires
        self.draw_copper_wires = draw_copper_wires
        self.light = light
        self.maximum_wire_distance = maximum_wire_distance
        self.radius_visualisation_picture = radius_visualisation_picture
        self.track_coverage_during_build_by_moving = track_coverage_during_build_by_moving


@prototype_subclass
class MiningDrill(EntityWithOwner):
    def __init__(self, name, type, energy_source, energy_usage, mining_speed, resource_categories, resource_searching_radius,
                 vector_to_place_result, allowed_effects=None, animations=None, base_picture=None, base_productivity=None,
                 base_render_layer=None, circuit_connector_sprites=None, circuit_wire_connection_points=None,
                 circuit_wire_max_distance=None, draw_circuit_wires=False, draw_copper_wires=False,
                 graphics_set=None, input_fluid_box=None, module_specification=None, monitor_visualization_tint=None,
                 output_fluid_box=None, radius_visualisation_picture=None, wet_mining_graphics_set=None,
                 allow_run_time_change_of_is_military_target=None, is_military_target=None, alert_when_damaged=None,
                 attack_reaction=None, corpse=None, create_ghost_on_death=None, damaged_trigger_effect=None,
                 dying_explosion=None, dying_trigger_effect=None, healing_per_tick=None, hide_resistances=None,
                 integration_patch=None, integration_patch_render_layer=None, loot=None, max_health=None,
                 random_corpse_variation=None, repair_sound=None, repair_speed_modifier=None, resistances=None,
                 icons=None, icon=None, icon_size=None, additional_pastable_entities=None, alert_icon_scale=None,
                 alert_icon_shift=None, allow_copy_paste=None, autoplace=None, build_base_evolution_requirement=None,
                 build_grid_size=None, build_sound=None, close_sound=None, collision_box=None, collision_mask=None,
                 created_effect=None, created_smoke=None, drawing_box=None, emissions_per_second=None,
                 enemy_map_color=None, fast_replaceable_group=None, flags=None, friendly_map_color=None,
                 hit_visualization_box=None, map_color=None, map_generator_bounding_box=None, minable=None,
                 mined_sound=None, mining_sound=None, next_upgrade=None, open_sound=None, placeable_by=None,
                 protected_from_tile_building=None, radius_visualisation_specification=None, remains_when_mined=None,
                 remove_decoratives=None, rotated_sound=None, selectable_in_game=None, selection_box=None,
                 selection_priority=None, shooting_cursor_size=None, sticker_box=None, subgroup=None,
                 tile_height=None, tile_width=None, trigger_target_mask=None, vehicle_impact_sound=None,
                 water_reflection=None, working_sound=None, localised_description=None, localised_name=None, order=None):
        super().__init__(name, type, allow_run_time_change_of_is_military_target, is_military_target, alert_when_damaged,
                         attack_reaction, corpse, create_ghost_on_death, damaged_trigger_effect, dying_explosion,
                         dying_trigger_effect, healing_per_tick, hide_resistances, integration_patch,
                         integration_patch_render_layer, loot, max_health, random_corpse_variation, repair_sound,
                         repair_speed_modifier, resistances, icons, icon, icon_size, additional_pastable_entities,
                         alert_icon_scale, alert_icon_shift, allow_copy_paste, autoplace, build_base_evolution_requirement,
                         build_grid_size, build_sound, close_sound, collision_box, collision_mask, created_effect,
                         created_smoke, drawing_box, emissions_per_second, enemy_map_color, fast_replaceable_group,
                         flags, friendly_map_color, hit_visualization_box, map_color, map_generator_bounding_box,
                         minable, mined_sound, mining_sound, next_upgrade, open_sound, placeable_by, protected_from_tile_building,
                         radius_visualisation_specification, remains_when_mined, remove_decoratives, rotated_sound,
                         selectable_in_game, selection_box, selection_priority, shooting_cursor_size, sticker_box,
                         subgroup, tile_height, tile_width, trigger_target_mask, vehicle_impact_sound, water_reflection,
                         working_sound, localised_description, localised_name, order)

        self.energy_source = energy_source
        self.energy_usage = energy_usage
        self.mining_speed = mining_speed
        self.resource_categories = resource_categories
        self.resource_searching_radius = resource_searching_radius
        self.vector_to_place_result = vector_to_place_result
        self.allowed_effects = allowed_effects
        self.animations = animations
        self.base_picture = base_picture
        self.base_productivity = base_productivity
        self.base_render_layer = base_render_layer
        self.circuit_connector_sprites = circuit_connector_sprites
        self.circuit_wire_connection_points = circuit_wire_connection_points
        self.circuit_wire_max_distance = circuit_wire_max_distance
        self.draw_circuit_wires = draw_circuit_wires
        self.draw_copper_wires = draw_copper_wires
        self.graphics_set = graphics_set
        self.input_fluid_box = input_fluid_box
        self.module_specification = module_specification
        self.monitor_visualization_tint = monitor_visualization_tint
        self.output_fluid_box = output_fluid_box
        self.radius_visualisation_picture = radius_visualisation_picture
        self.wet_mining_graphics_set = wet_mining_graphics_set
