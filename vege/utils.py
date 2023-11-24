from .models import Recipe
def add_dummy_recipes():
    recipes=[
        {
            "recipe_name": "Grilled Salmon with Lemon Dill Sauce",
            "recipe_description": "Delicious and healthy grilled salmon seasoned with a mix of herbs and served with a zesty lemon dill sauce. Perfect for a light and flavorful dinner."
        },
        {
            "recipe_name": "Mushroom Risotto with Parmesan Cheese",
            "recipe_description": "Creamy mushroom risotto made with Arborio rice, sautéed mushrooms, and a generous sprinkle of Parmesan cheese. A comforting and elegant dish for any occasion."
        },
        {
            "recipe_name": "Spicy Chickpea Curry",
            "recipe_description": "A flavorful and hearty chickpea curry with a kick of spice. Packed with aromatic Indian spices, tomatoes, and coconut milk, this vegan dish is a crowd-pleaser."
        },
        {
            "recipe_name": "Caprese Salad with Balsamic Glaze",
            "recipe_description": "A classic Caprese salad featuring fresh tomatoes, mozzarella cheese, and basil leaves drizzled with a balsamic glaze. A simple and refreshing appetizer or side dish."
        },
        {
            "recipe_name": "Homemade Margherita Pizza",
            "recipe_description": "Create the perfect Margherita pizza at home with a thin crust, tomato sauce, fresh mozzarella, and basil leaves. A delicious and satisfying homemade pizza experience."
        },{
        "recipe_name": "Lemon Garlic Herb Roasted Chicken",
        "recipe_description": "Tender and juicy roasted chicken marinated with a flavorful blend of lemon, garlic, and herbs. A simple yet impressive dish for a family dinner."
        },
        {
            "recipe_name": "Quinoa Salad with Avocado and Black Beans",
            "recipe_description": "A nutritious and colorful quinoa salad featuring ripe avocados, black beans, cherry tomatoes, and a zesty lime dressing. A great option for a light lunch or side dish."
        },
        {
            "recipe_name": "Thai Red Curry Shrimp",
            "recipe_description": "Spicy and aromatic Thai red curry with succulent shrimp, coconut milk, and a variety of vegetables. Serve over jasmine rice for a delicious and satisfying meal."
        },
        {
            "recipe_name": "Vegetarian Stuffed Bell Peppers",
            "recipe_description": "Bell peppers filled with a savory mixture of quinoa, black beans, corn, and spices. Baked to perfection and topped with melted cheese. A tasty vegetarian option."
        },
        {
            "recipe_name": "Homemade Beef and Vegetable Stir-Fry",
            "recipe_description": "Quick and easy beef and vegetable stir-fry with a savory soy-ginger sauce. Serve over rice or noodles for a speedy and delicious weeknight dinner."
        },
        {
            "recipe_name": "Cauliflower Crust Margherita Pizza",
            "recipe_description": "A low-carb twist on the classic Margherita pizza, featuring a cauliflower crust topped with tomato sauce, fresh mozzarella, and basil. Healthy and delicious."
        },
        {
            "recipe_name": "Pesto Pasta with Cherry Tomatoes and Pine Nuts",
            "recipe_description": "Al dente pasta tossed in a vibrant basil pesto sauce, cherry tomatoes, and toasted pine nuts. A simple and flavorful pasta dish that comes together in minutes."
        },
        {
            "recipe_name": "Honey Mustard Glazed Salmon",
            "recipe_description": "Pan-seared salmon glazed with a sweet and tangy honey mustard sauce. Served with roasted vegetables, this dish is a perfect combination of flavors and textures."
        },
        {
            "recipe_name": "Greek Salad with Feta and Kalamata Olives",
            "recipe_description": "A refreshing Greek salad featuring crisp cucumbers, ripe tomatoes, feta cheese, Kalamata olives, and a drizzle of olive oil. A light and healthy option for a summer day."
        },
        {
            "recipe_name": "Sweet Potato and Black Bean Tacos",
            "recipe_description": "Vegetarian tacos filled with roasted sweet potatoes, black beans, avocado, and a lime-cilantro dressing. A tasty and satisfying meat-free alternative."
        },
        {
            "recipe_name": "Teriyaki Chicken Skewers with Pineapple",
            "recipe_description": "Grilled teriyaki chicken skewers with chunks of sweet pineapple. The perfect balance of sweet and savory for a delightful barbecue or summer party."
        },
        {
            "recipe_name": "Butternut Squash Soup with Coconut Milk",
            "recipe_description": "Creamy and comforting butternut squash soup made with coconut milk and a blend of warm spices. A cozy soup for chilly evenings."
        },
        {
            "recipe_name": "Mango Avocado Salsa",
            "recipe_description": "A vibrant salsa with ripe mango, creamy avocado, red onion, cilantro, and lime juice. Serve with tortilla chips or as a topping for grilled chicken or fish."
        },
        {
            "recipe_name": "Chicken Caesar Salad Wrap",
            "recipe_description": "A classic Caesar salad with grilled chicken wrapped in a flour tortilla. A portable and satisfying lunch option for those on the go."
        },
        {
            "recipe_name": "Eggplant Parmesan",
            "recipe_description": "Slices of eggplant coated in breadcrumbs, baked to perfection, and layered with marinara sauce and melted mozzarella. A comforting and hearty vegetarian dish."
        },
        {
            "recipe_name": "Chickpea and Spinach Curry",
            "recipe_description": "A wholesome curry featuring chickpeas, spinach, and a blend of aromatic spices. Serve over rice or with naan bread for a nourishing and flavorful meal."
        },
        {
            "recipe_name": "Lentil and Vegetable Soup",
            "recipe_description": "A hearty soup made with lentils, carrots, celery, and tomatoes. Packed with protein and fiber, this soup is both nutritious and satisfying."
        },
        {
            "recipe_name": "Shrimp Scampi with Linguine",
            "recipe_description": "Linguine pasta tossed in a garlic and white wine sauce with succulent shrimp. A simple and elegant dish that comes together quickly for a weeknight dinner."
        },
        {
            "recipe_name": "Caprese Stuffed Chicken Breast",
            "recipe_description": "Chicken breasts stuffed with fresh mozzarella, cherry tomatoes, and basil. Baked until golden and juicy, this dish is a flavorful twist on the classic Caprese salad."
        },
        {
            "recipe_name": "Vegetable and Tofu Stir-Fry",
            "recipe_description": "A colorful stir-fry with a mix of vegetables and tofu in a savory soy-ginger sauce. Serve over rice or noodles for a delicious and wholesome vegetarian meal."
        },
        {
            "recipe_name": "Pumpkin Spice Pancakes",
            "recipe_description": "Fluffy pancakes infused with pumpkin puree and warm spices. Top with maple syrup and a dollop of whipped cream for a delightful autumn breakfast."
        },
        {
            "recipe_name": "Crispy Baked Zucchini Fries",
            "recipe_description": "Zucchini fries coated in a seasoned breadcrumb crust and baked until golden and crispy. A healthier alternative to traditional french fries, perfect for snacking."
        },
        {
            "recipe_name": "Sesame Ginger Glazed Salmon",
            "recipe_description": "Pan-seared salmon glazed with a savory sesame ginger sauce. Served with steamed broccoli and rice, this dish is a delicious and nutritious choice for dinner."
        },
        {
            "recipe_name": "Mediterranean Quinoa Bowl",
            "recipe_description": "A vibrant quinoa bowl with cherry tomatoes, cucumber, olives, feta cheese, and a lemon herb dressing. A nutritious and satisfying meal with Mediterranean flavors."
        },
        {
            "recipe_name": "Blueberry Almond Overnight Oats",
            "recipe_description": "A wholesome breakfast option with rolled oats, almond milk, blueberries, and a sprinkle of almonds. Prep the night before for a quick and nutritious morning meal."
        },
        {
            "recipe_name": "Cajun Shrimp and Sausage Skillet",
            "recipe_description": "A spicy and flavorful skillet dish featuring Cajun-seasoned shrimp, smoked sausage, bell peppers, and onions. Serve over rice or pasta for a bold and satisfying meal."
        },
        {
            "recipe_name": "Tomato Basil Bruschetta",
            "recipe_description": "Toasted baguette slices topped with a mixture of ripe tomatoes, fresh basil, garlic, and balsamic glaze. A simple and appetizing starter for any meal."
        },{
        "recipe_name": "Mango Coconut Chia Pudding",
        "recipe_description": "A tropical chia pudding made with coconut milk, ripe mango, and a hint of vanilla. A nutritious and delicious dessert or breakfast option."
        },
        {
            "recipe_name": "Beef and Broccoli Stir-Fry",
            "recipe_description": "Thin slices of beef stir-fried with broccoli in a savory soy-ginger sauce. Quick and easy to make, this stir-fry is a classic favorite."
        },
        {
            "recipe_name": "Cranberry Pecan Chicken Salad",
            "recipe_description": "A delightful chicken salad with dried cranberries, pecans, celery, and a creamy mayonnaise dressing. Perfect for sandwiches or served over a bed of greens."
        },
        {
            "recipe_name": "Garlic Parmesan Roasted Brussels Sprouts",
            "recipe_description": "Brussels sprouts roasted to perfection with garlic, Parmesan cheese, and a drizzle of balsamic glaze. A tasty and healthy side dish for any meal."
        },
        {
            "recipe_name": "Chocolate Avocado Smoothie",
            "recipe_description": "A creamy and indulgent smoothie made with ripe avocados, banana, cocoa powder, and almond milk. A delicious and nutritious treat for chocolate lovers."
        },
        {
            "recipe_name": "Chicken and Vegetable Kebabs",
            "recipe_description": "Skewers of marinated chicken and colorful vegetables grilled to perfection. A fun and flavorful dish for a barbecue or summer gathering."
        },
        {
            "recipe_name": "Spinach and Feta Stuffed Chicken Breast",
            "recipe_description": "Chicken breasts stuffed with a mixture of spinach, feta cheese, and garlic. Baked until golden and juicy, this dish is a tasty and elegant option for dinner."
        },
        {
            "recipe_name": "Blackberry Mint Lemonade",
            "recipe_description": "A refreshing lemonade infused with fresh blackberries and mint leaves. A delightful and colorful drink for a hot summer day or special occasion."
        },
        {
            "recipe_name": "Sausage and Kale Soup",
            "recipe_description": "A hearty soup with Italian sausage, kale, white beans, and flavorful herbs. Warm and comforting, this soup is perfect for chilly evenings."
        },
        {
            "recipe_name": "Roasted Vegetable and Hummus Wrap",
            "recipe_description": "A wholesome wrap filled with roasted vegetables, hummus, and a sprinkle of feta cheese. A delicious and satisfying option for a quick lunch or dinner."
        },
        {
            "recipe_name": "Peach and Raspberry Crisp",
            "recipe_description": "A fruity crisp featuring ripe peaches and juicy raspberries topped with a golden oat and almond crumble. Serve warm with a scoop of vanilla ice cream for a delightful dessert."
        },
        {
            "recipe_name": "Lemon Herb Grilled Chicken",
            "recipe_description": "Juicy chicken breasts marinated in a lemon and herb-infused mixture, then grilled to perfection. A light and flavorful dish for a summer barbecue."
        },
        {
            "recipe_name": "Vegetarian Lentil Loaf",
            "recipe_description": "A hearty lentil loaf packed with vegetables, herbs, and spices. A tasty and nutritious alternative to traditional meatloaf, perfect for a vegetarian or vegan meal."
        }
    ]
    
    try:
        for recipe in recipes:
            Recipe.objects.create(**recipe)
    except Exception as e:
        print(e)