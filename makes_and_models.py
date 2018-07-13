class MakesAndModels:
    """This reads the files models.txt and makes.txt and creates dictionary of them
    
    Methods:
    ---------
    read_models
    read_makes
    dict_makes_models
    """
    def read_models(self):
        with open("models.txt") as models:
            models_list = models.readlines()
            for model in models_list:
                print(model)
            return models_list

    def read_makes(self):
        with open("makes.txt") as makes:
            makes_list = makes.readlines()
            for make in makes_list:
                print(make)
            return makes_list


    def dict_makes_models(self):
        make_model_dict = dict()
        makes = self.read_makes()
        for make in makes:
            make_model_dict[make.strip()] = list()
        models = self.read_models()
        for model in models:
            model_name = model.split("=")[1].strip()
            first_letter=model.split("=")[0]
            for key in make_model_dict: 
                if key.startswith(first_letter):
                    make_model_dict[key].append(model_name)
        print(make_model_dict)

            

    # The dictionary keys will be the make names.
    # The value for each key will be a list of model names.
myClass = MakesAndModels()
myClass.dict_makes_models()