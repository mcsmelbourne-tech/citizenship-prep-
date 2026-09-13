import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="US Citizenship Test Prep Hub", page_icon="🇺🇸", layout="wide"
)

# Initialize Session State for Quiz Scores
if "civics_score" not in st.session_state:
    st.session_state.civics_score = 0
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False

st.title("🇺🇸 U.S. Citizenship & Naturalization Prep Hub")
st.markdown(
    "Your all-in-one companion for mastering the N-400 review, Civics exam, and English Reading/Writing tests."
)

# Sidebar Navigation Tabs
tabs = st.tabs(
    [
        "📋 N-400 Application Review",
        "🏛️ Civics Practice Test",
        "📖 Reading & Writing Test",
        "💡 Interview Tips",
    ]
)

# ---------------------------------------------------------
# TAB 1: N-400 Application & Background Review
# ---------------------------------------------------------
with tabs[0]:
  st.header("Form N-400 Application Reviewer")
  st.markdown(
      "The officer will ask questions based directly on your submitted N-400"
      " application. Review these crucial definitions and parts."
  )

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Key Terms & Definitions")
    with st.expander("What does 'Oath of Allegiance' mean?"):
      st.write(
          "A promise to be loyal to the United States and support the U.S."
          " Constitution."
      )
    with st.expander("What is 'Form of Government of the U.S.'?"):
      st.write("Republic / Democracy / Constitution-based federal republic.")
    with st.expander("What does 'Perjury' mean?"):
      st.write(
          "Making a false statement while under oath (lying intentionally"
          " after promising to tell the truth)."
      )
    with st.expander("What does 'Non-U.S. National' mean?"):
      st.write(
          "Someone born in an outlying possession of the U.S. (such as American"
          " Samoa)."
      )

  with col2:
    st.subheader("Common Background Check Questions")
    st.markdown("""
        Be prepared to confirm or explain these items if they apply to you:
        * Have you ever claimed to be a U.S. citizen?
        * Have you ever failed to file a federal, state, or local tax return?
        * Have you ever been a member of, or associated with, any organization, association, fund, foundation, party, club, society, or similar group?
        * Are you willing to bear arms on behalf of the United States?
        * Are you willing to perform noncombatant services in the U.S. Armed Forces?
        """)

# ---------------------------------------------------------
# TAB 2: Civics Practice Test (100 Questions Bank Sample)
# ---------------------------------------------------------
with tabs[1]:
  st.header("Civics Test Practice (100 Questions)")
  st.markdown(
      "The USCIS officer will orally ask you up to 10 questions from the 100"
      " civics questions. You must get 6 correct to pass."
  )

  # Sample Question Database
  civics_db = [
      {
          "q": "What is the supreme law of the land?",
          "a": "The Constitution",
      },
      {
          "q": "What does the Constitution do?",
          "a": (
              "Sets up the government, defines the government, protects basic"
              " rights of Americans"
          ),
      },
      {
          "q": (
              "The idea of self-government is in the first three words of the"
              " Constitution. What are these words?"
          ),
          "a": "We the People",
      },
      {"q": "What is an amendment?", "a": "A change or addition to the Constitution"},
      {"q": "What do we call the first ten amendments to the Constitution?", "a": "The Bill of Rights"},
      {
          "q": (
              "What is one right or freedom from the First Amendment?*"
          ),
          "a": (
              "Speech, Religion, Assembly, Press, Petition the government"
          ),
      },
      {"q": "How many amendments does the Constitution have?", "a": "Twenty-seven (27)"},
      {
          "q": "What did the Declaration of Independence do?",
          "a": (
              "Announced our independence from Great Britain, declared our"
              " independence, said that the United States is free"
          ),
      },
      {
          "q": "What are two rights in the Declaration of Independence?",
          "a": "Life, liberty, pursuit of happiness",
      },
      {"q": "What is freedom of religion?", "a": "You can practice any religion, or not practice a religion."},
  ]

  selected_q = st.selectbox(
      "Choose a question to practice:",
      options=range(len(civics_db)),
      format_func=lambda x: civics_db[x]["q"],
  )

  if st.button("Reveal Answer"):
    st.success(f"**Answer:** {civics_db[selected_q]['a']}")

  st.divider()
  st.subheader("Simulate a Mini-Quiz (10 Random Questions)")
  if st.button("Start Random Quiz"):
    st.session_state.quiz_sample = random.sample(
        civics_db, min(3, len(civics_db))
    )
    st.session_state.quiz_active = True

  if st.session_state.get("quiz_active", False):
    for i, item in enumerate(st.session_state.quiz_sample):
      st.markdown(f"**Q{i+1}: {item['q']}**")
      st.text_input(f"Your answer for Q{i+1}", key=f"user_ans_{i}")
      with st.expander(f"Check Answer Q{i+1}"):
        st.info(item["a"])

# ---------------------------------------------------------
# TAB 3: English Reading & Writing Test Practice
# ---------------------------------------------------------
with tabs[2]:
  st.header("English Reading & Writing Practice")
  st.markdown(
      "You must read 1 out of 3 sentences correctly, and"
      " write 1 out of 3 sentences correctly dictated by the officer."
  )

  col_r, col_w = st.columns(2)

  with col_r:
    st.subheader("📖 Reading Practice Generator")
    reading_sentences = [
        "Abraham Lincoln was the President during the Civil War.",
        "Citizens have the right to vote.",
        "The capital of the United States is Washington, D.C.",
        "The American flag has red, white, and blue stripes.",
        "Thanksgiving is a national holiday in November.",
    ]
    if st.button("Generate Random Reading Sentence"):
      st.session_state.current_reading = random.choice(reading_sentences)

    if "current_reading" in st.session_state:
      st.markdown(
          "> **Read this sentence out loud:**"
          f" `{st.session_state.current_reading}`"
      )

  with col_w:
    st.subheader("✍️ Writing Practice Dictation")
    writing_sentences = [
        "George Washington is the father of our country.",
        "The United States has fifty states.",
        "Citizens vote in November.",
        "Freedom of speech is an important right.",
        "Washington is our first president.",
    ]
    if st.button("Get Dictation Prompt"):
      st.session_state.current_writing = random.choice(writing_sentences)

    if "current_writing" in st.session_state:
      st.info(
          "🔊 *Listen to the prompt (simulated):* Write down: [Secret Sentence"
          " Dictation]"
      )
      user_input_write = st.text_input("Type what you hear:")
      if st.button("Check Writing"):
        if (
            user_input_write.strip().lower()
            == st.session_state.current_writing.strip().lower()
        ):
          st.success("Correct! Great spelling and capitalization.")
        else:
          st.error(
              f"Not quite. The correct sentence was:"
              f" '{st.session_state.current_writing}'"
          )

# ---------------------------------------------------------
# TAB 4: Interview Tips
# ---------------------------------------------------------
with tabs[3]:
  st.header("Naturalization Interview Tips")
  st.markdown("""
    * **Dress Appropriately:** Dress in standard business-casual attire.
    * **Bring Required Documents:** Bring your Green Card (Permanent Resident Card), state ID, and all relevant passport/travel documents.
    * **Arrive Early:** Aim to arrive at the USCIS field office at least 30 minutes before your scheduled appointment window.
    * **Ask for Clarification:** If you do not understand a question asked by the officer, politely ask: *"Could you please rephrase or repeat that question?"*
    """)
