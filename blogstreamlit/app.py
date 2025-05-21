#cd D:\Blogging\blogapi
#mvn spring-boot:run   to run the project do this 
import streamlit as st
import requests

BASE_URL = "https://blog-backend-5auv.onrender.com/api/posts"

st.set_page_config(page_title="Blog Manager", layout="wide")
st.title("📘 Blogging Platform (Streamlit Frontend)")

tab1, tab2, tab3, tab4 = st.tabs(["📄 View Posts", "➕ Create Post", "✏️ Edit Post", "🗑️ Delete Post"])

# View Posts
with tab1:
    st.subheader("All Blog Posts")
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        posts = response.json()

        if not posts:
            st.info("No posts available.")
        for post in posts:
            with st.expander(post['title']):
                st.write(post['content'])
                st.caption(f"Author: {post['author']}")
                st.markdown("---")
    except Exception as e:
        st.error(f"Failed to fetch posts: {e}")

# Create Post
with tab2:
    st.subheader("Create New Post")
    with st.form("create_form"):
        title = st.text_input("Title")
        content = st.text_area("Content")
        author = st.text_input("Author")
        submit = st.form_submit_button("Create Post")

        if submit:
            data = {"title": title, "content": content, "author": author}
            res = requests.post(BASE_URL, json=data)
            if res.status_code == 201:
                st.success("✅ Post created successfully!")
            else:
                st.error("❌ Failed to create post")

# Edit Post
# Edit Post
with tab3:
    st.subheader("Edit Existing Post")

    # Fetch and list all posts for user to select
    try:
        list_res = requests.get(BASE_URL)
        list_res.raise_for_status()
        posts = list_res.json()

        if not posts:
            st.info("No posts to edit.")
        else:
            # Build dropdown options like "My First Blog (ID: 1)"
            post_options = {f"{post['title']} (ID: {post['id']})": post['id'] for post in posts}
            selected = st.selectbox("Choose a post to edit", list(post_options.keys()))
            post_id = post_options[selected]

            # Fetch selected post details
            res = requests.get(f"{BASE_URL}/{post_id}")
            if res.status_code == 200:
                post = res.json()
                with st.form("edit_form"):
                    new_title = st.text_input("Title", value=post['title'])
                    new_content = st.text_area("Content", value=post['content'])
                    new_author = st.text_input("Author", value=post['author'])
                    update = st.form_submit_button("Update Post")

                    if update:
                        updated_data = {
                            "title": new_title,
                            "content": new_content,
                            "author": new_author
                        }
                        update_res = requests.put(f"{BASE_URL}/{post_id}", json=updated_data)
                        if update_res.status_code == 200:
                            st.success("✅ Post updated successfully!")
                        else:
                            st.error("❌ Failed to update post")
            else:
                st.warning("⚠️ Failed to fetch selected post.")

    except Exception as e:
        st.error(f"Failed to load posts: {e}")
# Delete Post
# Delete Post
with tab4:
    st.subheader("Delete a Post")

    # Fetch and display posts in a dropdown
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        posts = response.json()

        if posts:
            post_options = {f"{post['title']} (ID: {post['id']})": post['id'] for post in posts}
            selected = st.selectbox("Select a Post to Delete", list(post_options.keys()))
            del_id = post_options[selected]

            if st.button("Delete Post"):
                del_res = requests.delete(f"{BASE_URL}/{del_id}")
                if del_res.status_code == 200:
                    st.success("✅ Post deleted successfully!")
                else:
                    st.error("❌ Failed to delete post")
        else:
            st.info("No posts available to delete.")
    except Exception as e:
        st.error(f"Failed to load posts: {e}")
