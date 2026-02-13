import streamlit as st
from github import Github

def upload_to_github(data):
    token = st.secrets["GITHUB_TOKEN"]
    g = Github(token)

    repo = g.get_repo("PetrucKlouxie/test1")
    file_path = "data.csv"

    try:
        file = repo.get_contents(file_path)
        content = file.decoded_content.decode()
        new_content = content + data + "\n"

        repo.update_file(
            file_path,
            "Update via Streamlit",
            new_content,
            file.sha
        )
    except:
        repo.create_file(
            file_path,
            "Create data file",
            "nama,umur\n" + data + "\n"
        )

st.title("Form Input")

nama = st.text_input("Nama")
umur = st.number_input("Umur", 0)

if st.button("Submit"):
    upload_to_github(f"{nama},{umur}")
    st.success("Data tersimpan ke GitHub!")
