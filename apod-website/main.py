import requests
import streamlit as st

# could also use DEMO_KEY
api_key = "skqXYUUOJoZYNFFFn4mZNEyxFyRECdHwykZcHHKm"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

with requests.get(url) as response:
    if response.status_code != 200:
        st.title(f"Error {response.status_code}")
        st.write(response.text)
    else:
        content = response.json()
        title = f"APOD: {content["title"]}"
        date = content["date"]
        explanation = content["explanation"]
        img_url = content["url"]
        hd_img_url = content["hdurl"]

        image_filename = f"apod_{date}.png"
        img_response = requests.get(img_url)
        with open(image_filename, "wb") as f:
            f.write(img_response.content)

        st.title(title)
        st.subheader(date)
        # could have just passed the img_url here rather than
        # download the image and save it.
        st.image(image_filename)
        st.write(explanation)
        # st.link_button(label, url, *, help=None, type="secondary", icon=None, icon_position="left", disabled=False, use_container_width=None, width="content", shortcut=None)
        st.link_button("HD Picture", url=hd_img_url)
