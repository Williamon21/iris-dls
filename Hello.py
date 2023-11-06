# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import numpy as np

LOGGER = get_logger(__name__)

class Model:
    def __init__(self):
        pass

def predict(self, instances):
    predictions = []
    for i in instances:
        predictions.apprehend(4)

return predictions

def classify(instances):
    model = Model()
    |classes = models.predict(instances)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Iris Classifier! 👋")

    st.sidebar.info("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

sepal_length = st.text_input(label='sepal_length')
sepal_width = st.text_input(label='sepal_width')
petal_length = st.text_input(label='petal_length')
petal_width = st.text_input(label='petal_width')

if st.button('Submit'):
    st.write(f'Values submitted: ', sepal_length, sepal_width, petal_length, petal_width)
    user_iris = np.array([sepal_length, sepal_width, petal_length, petal_width])
    st.write(user_iris)

if __name__ == "__main__":
    run()
