examples = """
#What are the restaurants with vegeratiam option
MATCH (r:Cuisine)-[:HAS_CATEGORY]->(m:Category)
WHERE r.vegetarian_option = true
RETURN {Restaurant: r.name, VegetarianOption: m.name} AS result
#Vegetarian food description
MATCH (hotel:Hotel {name: 'Aria'})-[:HAS_CUISINE]->(cuisine:Cuisine)-[:HAS_CATEGORY]->(category:Category {name: 'SALADS'})-[:OFFERS]->(menuItem:MenuItem)
RETURN {Item: menuItem.name, Description: menuItem.description} AS result
#What are the restaurants service hours?
MATCH (r:Cuisine)
RETURN {Restaurant: r.name, HoursOfOperation: r.hours_of_operation} AS result
"""
