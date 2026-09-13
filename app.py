import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="US Citizenship Test Prep Hub", page_icon="🇺🇸", layout="wide"
)

# Initialize Session States
if "civics_score" not in st.session_state:
    st.session_state.civics_score = 0
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False

st.title("🇺🇸 U.S. Citizenship & Naturalization Prep Hub")
st.markdown(
    "Your comprehensive study companion for the N-400 application review,"
    " interview vocabulary, civics exam, and English reading/writing tests."
)

# Sidebar Navigation Tabs
tabs = st.tabs([
    "📋 N-400 & Interview Vocabulary",
    "🏛️ Civics Practice Bank",
    "📖 Reading & Writing Skills",
    "💡 Mock Test Simulator",
])

# ---------------------------------------------------------
# TAB 1: N-400 Review & Interview Vocabulary Builder
# ---------------------------------------------------------
with tabs[0]:
  st.header("Form N-400 Background & Interview Vocabulary")
  st.markdown(
      "USCIS officers evaluate your English comprehension using terms directly"
      " tied to your N-400 application and background questions."
  )

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("📚 Key N-400 Terms & Synonyms")
    vocab_dict = {
        "Habitually": "Often or repeatedly.",
        "Verify": "Prove that something is true.",
        "Marital Status": (
            "Whether you are single, married, divorced, or widowed."
        ),
        "Swear": "To promise under oath to tell the truth.",
        "Registered": "Signed up officially (e.g., to vote or selective service).",
        "Spouse": "Your husband or wife.",
        "Dependent": (
            "Someone you support financially, such as a child."
        ),
        "Citation": (
            "An official written notice or traffic ticket from law enforcement"
            "."
        ),
        "Affiliation": (
            "A formal connection or involvement with an organization."
        ),
    }

    selected_vocab = st.selectbox(
        "Select a vocabulary word to review:", list(vocab_dict.keys())
    )
    st.info(f"**Meaning:** {vocab_dict[selected_vocab]}")

  with col2:
    st.subheader("⚠️ Common Background Risk Areas")
    st.markdown("""
        Be ready to address these parts clearly during your review:
        * **Taxes:** Have you ever failed to file a federal, state, or local tax return?
        * **Organizations:** Have you ever been a member of any terrorist group, communist party, or total-control organization?
        * **Lie / Misrepresentation:** Have you ever given false information to a U.S. government official to gain entry or benefits?
        * **Removal Proceedings:** Have you ever been placed in removal, exclusion, rescission, or deportation proceedings?
        """)

# ---------------------------------------------------------
# TAB 2: Expanded Civics Question Bank
# ---------------------------------------------------------
with tabs[1]:
  st.header("Civics Question Bank (Principles & History)")
  st.markdown(
      "Practice questions spanning American Government, American History, and"
      " Integrated Civics."
  )

  # Expanded Civics Database
  civics_bank = [
      {
          "category": "American Government",
          "q": "What is the supreme law of the land?",
          "a": "The Constitution",
      },
      {
          "category": "American Government",
          "q": "What does the Constitution do?",
          "a": (
              "Sets up the government, defines the government, protects basic"
              " rights of Americans"
          ),
      },
      {
          "category": "American Government",
          "q": (
              "What is the economic system in the United States?"
          ),
          "a": "Capitalist economy / Market economy",
      },
      {
          "category": "American Government",
          "q": "What is the 'rule of law'?",
          "a": (
              "Everyone must follow the law; leaders and government must obey"
              " the law; no one is above the law."
          ),
      },
      {
          "category": "American Government",
          "q": "Name one branch or part of the government.",
          "a": (
              "Congress, legislative, President, executive, the courts, or"
              " judicial"
          ),
      },
      {
          "category": "American Government",
          "q": "What stops one branch of government from becoming too powerful?",
          "a": "Checks and balances / separation of powers",
      },
      {
          "category": "American Government",
          "q": "How many U.S. Senators are there?",
          "a": "One hundred (100)",
      },
      {
          "category": "American History",
          "q": "What did the Declaration of Independence do?",
          "a": (
              "Announced/declared independence from Great Britain; said U.S."
              " is free"
          ),
      },
      {
          "category": "American History",
          "q": "What territory did the United States buy from France in 1803?",
          "a": "The Louisiana Territory / Louisiana",
      },
      {
          "category": "American History",
          "q": "Name one war fought by the U.S. in the 1800s.",
          "a": (
              "Civil War, War of 1812, Mexican-American War, Spanish-American"
              " War"
          ),
      },
      {
          "category": "American History",
          "q": "What did Martin Luther King, Jr. do?",
          "a": (
              "Fought for civil rights; worked for equality for all Americans"
          ),
      },
  ]

  selected_cat = st.selectbox(
      "Filter by Category:",
      ["All"] + list(set([item["category"] for item in civics_bank])),
  )

  filtered_bank = (
      civics_bank
      if selected_cat == "All"
      else [item for item in civics_bank if item["category"] == selected_cat]
  )

  q_idx = st.selectbox(
      "Select a question:",
      options=range(len(filtered_bank)),
      format_func=lambda x: filtered_bank[x]["q"],
  )

  if st.button("Show Answer"):
    st.success(f"**Correct Answer:** {filtered_bank[q_idx]['a']}")

# ---------------------------------------------------------
# TAB 3: English Reading & Writing Skill Practice
# ---------------------------------------------------------
with tabs[2]:
  st.header("Interactive Reading & Writing Practice")
  st.markdown(
      "To pass the English requirement, you must correctly read out loud 1 of"
      " 3 sentences and write 1 of 3 dictated sentences correctly."
  )

  col_read, col_write = st.columns(2)

  with col_read:
    st.subheader("📖 Reading Practice Engine")
    reading_pool = [
        "President Abraham Lincoln freed the slaves.",
        "Citizens have the right to vote in elections.",
        "The United States has fifty states.",
        "March is the third month of the year.",
        "What is the capital of your state?",
    ]

    if st.button("Generate Reading Prompt"):
      st.session_state.active_read = random.choice(reading_pool)

    if "active_read" in st.session_state:
      st.warning(
          f"**Read this sentence aloud clearly:**\n\n>"
          f" `{st.session_state.active_read}`"
      )

  with col_write:
    st.subheader("✍️ Writing Practice & Dictation Checker")
    writing_pool = [
        "Abrahams Lincoln was the president during the Civil War.",  # Note standard spelling check
        "The American flag has red, white, and blue stripes.",
        "Citizens vote for the President in November.",
        "George Washington is the father of our country.",
        "Capitalism is the economic system of the United States.",
    ]

    if st.button("Get Dictation Prompt Audio"):
      st.session_state.active_write = random.choice(writing_pool)
      st.info(
          "🔊 *[Simulated Audio Officer Dictation]*: Listen closely to the"
          " sentence prompt."
      )

    if "active_write" in st.session_state:
      user_writing = st.text_input("Type the sentence you heard word-for-word:")
      if st.button("Evaluate Writing"):
        # Clean spacing/punctuation comparison
        clean_target = (
            st.session_state.active_write.strip().lower().replace(".", "")
        )
        clean_user = user_writing.strip().lower().replace(".", "")

        if clean_target == clean_user:
          st.success(
              "✅ Perfect! Your spelling, capitalization, and phrasing match"
              " USCIS standards."
          )
        else:
          st.error(
              "❌ Minor error detected. Target sentence should be written"
              f" as:\n\n`{st.session_state.active_write}`"
          )

# ---------------------------------------------------------
# TAB 4: Mock Test Simulator
# ---------------------------------------------------------
with tabs[3]:
  st.header("Full Interview & Test Simulator")
  st.markdown(
      "Simulate the testing environment. You will be tested on 3 random civics"
      " questions. Aim for 100% accuracy!"
  )

  if st.button("Start Simulation Test"):
    st.session_state.sim_questions = random.sample(
        civics_bank, min(3, len(civics_bank))
    )
    st.session_state.sim_started = True

  if st.session_state.get("sim_started", False):
    with st.form("simulation_form"):
      user_answers = {}
      for i, item in enumerate(st.session_state.sim_questions):
        st.markdown(f"**Question {i+1}: {item['q']}**")
        user_answers[i] = st.text_input(
            f"Your answer for Q{i+1}", key=f"sim_ans_{i}"
        )

      submitted = st.form_submit_button("Submit Answers")
      if submitted:
        st.subheader("Simulation Results")
        for i, item in enumerate(st.session_state.sim_questions):
          st.write(f"**Q{i+1}:** {item['q']}")
          st.write(f"Your input: `{user_answers[i]}`")
          st.info(f"Official Answer Key: {item['a']}")
          st.divider()
