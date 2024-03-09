
import random
import pandas as pd

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

data["robot"] = (data["whoAmI"] == "robot").astype(int)
data["human"] = (data["whoAmI"] == "human").astype(int)


print(data.head(10))