from flask_restplus import fields, Namespace


class UserDto():
    user_ns = Namespace("user function", description="User registration, login, logout, change password")

    user_token_model = user_ns.model("user_token_model",
                                     {
                                         "token": fields.String

                                     })

    user_model = user_ns.model("login_model",
                               {
                                   "username": fields.String,
                                   "email": fields.String,
                                   "id": fields.Integer,
                                   "token": fields.String,
                                   "message": fields.String
                               })
    user_login_data_model_expect = user_ns.model("user_login_data_model_expect",
                                                 {
                                                     "username": fields.String,
                                                     "password": fields.String,
                                                 })

    user_list_model = user_ns.model("user list",
                                    {
                                        "total_number": fields.Integer,
                                        "users": fields.List(fields.Nested(user_model))

                                    })
    user_Forgetpassword_data_model_expect = user_ns.model("user_Forgetpassword_data_model_expect",
                                                          {"username": fields.String,
                                                           "email": fields.String,
                                                           })
    user_UserSignup_model_response = user_ns.model("user_UserSignup_data_model_expect",
                                                   {
                                                       "username": fields.String,
                                                       "message": fields.String,
                                                   })
    user_Forgetpassword_model_response = user_ns.model("user_Forgetpassword_model_response",
                                                       {
                                                           "username": fields.String,
                                                           "password": fields.String,
                                                           "message": fields.String
                                                       })

    user_ChangPassword_model_response = user_ns.model("user_ChangPassword_model_response",
                                                      {
                                                          "username": fields.String,
                                                          "new_password": fields.String,
                                                          "message": fields.String
                                                      })
    user_UserSignup_data_model_expect = user_ns.model("user_UserSignup_data_model_expect",
                                                      {
                                                          "username": fields.String,
                                                          "password1": fields.String,
                                                          "password2": fields.String,
                                                          "email": fields.String,
                                                      })
    user_ChangPassword_data_model_expect = user_ns.model("user_ChangPassword_data_model_expect",
                                                         {
                                                             "old_password": fields.String,
                                                             "new_password": fields.String,
                                                         })


class RecipeDto():
    Recipe_ns = Namespace("Recipe function", description="Recipe information,upload,search")

    Recipe_model_upload = Recipe_ns.model("Recipe_model_upload",
                                          {
                                              "R_name": fields.String,
                                              "R_description": fields.String,
                                              "R_category": fields.String,
                                              "R_calorie": fields.String,
                                              "image_id": fields.String,
                                              "user_id": fields.Integer,
                                              "R_igd_list": fields.String
                                          })

    Recipe_model = Recipe_ns.model("Recipe_model",
                                   {
                                       "R_name": fields.String,
                                       "R_description": fields.String,
                                       "R_category": fields.String,
                                       "R_calorie": fields.String,
                                       "R_img_url": fields.String,
                                       "user_id": fields.Integer,
                                       "id": fields.Integer
                                   })
    search_list_Recipe_model = Recipe_ns.model("search_list_Recipe_model",
                                   {
                                       "R_name": fields.String,
                                       "R_category": fields.String,
                                       "R_calorie": fields.String,
                                       "R_img_url": fields.String,
                                   })
    Ingredient_model = Recipe_ns.model("Ingredient_model",
                                       {
                                           "igd_name": fields.String,
                                           "igd_category": fields.String,
                                           "igd_calorie": fields.Integer,
                                           "igd_opponent": fields.String,
                                           "igb_description": fields.String,
                                           "igd_img_url": fields.String,
                                           "id": fields.Integer
                                       })
    Ingredient_model_upload = Recipe_ns.model("Ingredient_model_upload",
                                              {
                                                  "igd_name": fields.String,
                                                  "igd_category": fields.String,
                                                  "igd_calorie": fields.Integer,
                                                  "igd_opponent": fields.String,
                                                  "image_id": fields.String,
                                                  "id": fields.Integer
                                              })

    recipe_list_model = Recipe_ns.model("Recipe list",
                                        {
                                            "total_number": fields.Integer,
                                            "Recipes": fields.List(fields.Nested(Recipe_model))

                                        })


class SearchDto():
    search_ns = Namespace("search function", description="select igd,recipe")

    search_igd_model = search_ns.model("search_igd_model",
                                     {
                                         "igd_name": fields.String
                                     })



    search_igd_list_model = search_ns.model("search_igd_list_model",
                                            {
                                                "number":fields.Integer,
                                                "igd_list":fields.List(fields.Nested(search_igd_model))
                                            })
    search_recipe_model = search_ns.model("search_recipe_model",
                                     {
                                         "igd_name": fields.String,
                                         "R_category":fields.String
                                     })

    search_recipe_list_model_response = search_ns.model("search_recipe_list_model_response",
                                                        {
                                                            "recipe_list":fields.List(fields.Nested(RecipeDto.search_list_Recipe_model))
                                                        })


