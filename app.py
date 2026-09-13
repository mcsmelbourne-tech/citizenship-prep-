import random
import streamlit as st
import streamlit.components.v1 as components

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
# TAB 2: Expanded Civics Question Bank (Full Official Pool)
# ---------------------------------------------------------
with tabs[1]:
  st.header("Civics Question Bank (Principles & History)")
  st.markdown(
      "Practice questions spanning American Government, American History, and"
      " Integrated Civics."
  )

  # Comprehensive Civics Database
  civics_bank = [
      # American Government - Principles of Democracy
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
          "q": "The idea of self-government is in the first three words of the Constitution. What are these words?",
          "a": "We the People",
      },
      {
          "category": "American Government",
          "q": "What is an amendment?",
          "a": "A change (to the Constitution) or an addition (to the Constitution)",
      },
      {
          "category": "American Government",
          "q": "What do we call the first ten amendments to the Constitution?",
          "a": "The Bill of Rights",
      },
      {
          "category": "American Government",
          "q": "What is one right or freedom from the First Amendment?",
          "a": "Speech, religion, assembly, press, petition the government",
      },
      {
          "category": "American Government",
          "q": "How many amendments does the Constitution have?",
          "a": "Twenty-seven (27)",
      },
      {
          "category": "American Government",
          "q": "What did the Declaration of Independence do?",
          "a": (
              "Announced our independence from Great Britain, declared our"
              " independence, said that the United States is free"
          ),
      },
      {
          "category": "American Government",
          "q": "What are two rights in the Declaration of Independence?",
          "a": "Life, liberty, pursuit of happiness",
      },
      {
          "category": "American Government",
          "q": "What is freedom of religion?",
          "a": (
              "You can practice any religion, or not practice a religion."
          ),
      },
      {
          "category": "American Government",
          "q": "What is the economic system in the United States?",
          "a": "Capitalist economy / Market economy",
      },
      {
          "category": "American Government",
          "q": "What is the 'rule of law'?",
          "a": (
              "Everyone must follow the law; leaders, government, and no one"
              " is above the law."
          ),
      },
      # System of Government
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
          "q": "Who is in charge of the executive branch?",
          "a": "The President",
      },
      {
          "category": "American Government",
          "q": "Who makes federal laws?",
          "a": "Congress (Senate and House of Representatives)",
      },
      {
          "category": "American Government",
          "q": "What are the two parts of the U.S. Congress?",
          "a": "The Senate and House of Representatives",
      },
      {
          "category": "American Government",
          "q": "How many U.S. Senators are there?",
          "a": "One hundred (100)",
      },
      {
          "category": "American Government",
          "q": "We elect a U.S. Senator for how many years?",
          "a": "Six (6)",
      },
      {
          "category": "American Government",
          "q": "The House of Representatives has how many voting members?",
          "a": "Four hundred thirty-five (435)",
      },
      {
          "category": "American Government",
          "q": "We elect a U.S. Representative for how many years?",
          "a": "Two (2)",
      },
      {
          "category": "American Government",
          "q": "Who does a U.S. Senator represent?",
          "a": "All people of the state",
      },
      {
          "category": "American Government",
          "q": "Why do some states have more Representatives than other states?",
          "a": (
              "Because of the state's population, because they have more people"
          ),
      },
      {
          "category": "American Government",
          "q": "We elect a President for how many years?",
          "a": "Four (4)",
      },
      {
          "category": "American Government",
          "q": "In what month do we vote for President?",
          "a": "November",
      },
      {
          "category": "American Government",
          "q": "What is the name of the President of the United States now?",
          "a": "Check current office holder (Joe Biden / current sitting president)",
      },
      {
          "category": "American Government",
          "q": "What is the name of the Vice President of the United States now?",
          "a": "Check current office holder",
      },
      {
          "category": "American Government",
          "q": "If the President can no longer serve, who becomes President?",
          "a": "The Vice President",
      },
      {
          "category": "American Government",
          "q": "If both the President and the Vice President can no longer serve, who becomes President?",
          "a": "The Speaker of the House",
      },
      {
          "category": "American Government",
          "q": "Who is the Commander in Chief of the military?",
          "a": "The President",
      },
      {
          "category": "American Government",
          "q": "Who signs bills to become laws?",
          "a": "The President",
      },
      {
          "category": "American Government",
          "q": "Who vetoes bills?",
          "a": "The President",
      },
      {
          "category": "American Government",
          "q": "What does the President's Cabinet do?",
          "a": "Advises the President",
      },
      {
          "category": "American Government",
          "q": "What are two cabinet-level positions?",
          "a": (
              "Secretary of Agriculture, Secretary of Commerce, Secretary of"
              " Defense, Secretary of Education, Secretary of Energy, Secretary"
              " of Health and Human Services, Secretary of Homeland Security,"
              " Secretary of Housing and Urban Development, Secretary of the"
              " Interior, Secretary of Labor, Secretary of State, Secretary of"
              " Transportation, Secretary of the Treasury, Secretary of"
              " Veterans Affairs, Attorney General, Vice President"
          ),
      },
      {
          "category": "American Government",
          "q": "What does the judicial branch do?",
          "a": (
              "Reviews laws, explains laws, resolves disputes, decides if a"
              " law goes against the Constitution"
          ),
      },
      {
          "category": "American Government",
          "q": "What is the highest court in the United States?",
          "a": "The Supreme Court",
      },
      {
          "category": "American Government",
          "q": "How many justices are on the Supreme Court?",
          "a": "Check current court composition (typically nine / 9)",
      },
      {
          "category": "American Government",
          "q": "Under our Constitution, some powers belong to the federal government. What is one power of the federal government?",
          "a": (
              "To print money, to declare war, to create an army, to make"
              " treaties"
          ),
      },
      {
          "category": "American Government",
          "q": "Under our Constitution, some powers belong to the states. What is one power of the states?",
          "a": (
              "Provide schooling and education, provide protection (police),"
              " provide safety (fire departments), give a driver's license,"
              " approve zoning and land use"
          ),
      },
      {
          "category": "American Government",
          "q": "Who is the Governor of your state now?",
          "a": "Answers will vary by state.",
      },
      {
          "category": "American Government",
          "q": "What is the capital of your state?",
          "a": "Answers will vary by state.",
      },
      # American History - Colonial Period and Independence
      {
          "category": "American History",
          "q": "What are two major political parties in the United States?",
          "a": "Democratic and Republican",
      },
      {
          "category": "American History",
          "q": "What is the political party of the President now?",
          "a": "Check current party affiliation",
      },
      {
          "category": "American History",
          "q": "What is the name of the Speaker of the House of Representatives now?",
          "a": "Check current office holder",
      },
      {
          "category": "American History",
          "q": "There are four amendments to the Constitution about who can vote. Describe one of them.",
          "a": (
              "Citizens eighteen (18) and older can vote; You don't have to pay"
              " (a poll tax) to vote; Any citizen can vote (women and men);"
              " A male citizen of any race can vote."
          ),
      },
      {
          "category": "American History",
          "q": "What is one responsibility that is only for United States citizens?",
          "a": "Serve on a jury, vote in a federal election",
      },
      {
          "category": "American History",
          "q": "Name one right only for United States citizens.",
          "a": "Vote in a federal election, run for federal office",
      },
      {
          "category": "American History",
          "q": "What are two rights of everyone living in the United States?",
          "a": (
              "Freedom of expression, freedom of speech, freedom of assembly,"
              " freedom to petition the government, freedom of religion, the"
              " right to bear arms"
          ),
      },
      {
          "category": "American History",
          "q": "What do we show loyalty to when we say the Pledge of Allegiance?",
          "a": "The United States, the flag",
      },
      {
          "category": "American History",
          "q": "What is one promise you make when you become a United States citizen?",
          "a": (
              "Give up loyalty to other countries, defend the Constitution and"
              " laws of the United States, obey the laws of the United States,"
              " serve in the U.S. military (if needed), serve (do important"
              " work for) the nation, be loyal to the United States"
          ),
      },
      {
          "category": "American History",
          "q": "How old do citizens have to be to vote for President?",
          "a": "Eighteen (18) and older",
      },
      {
          "category": "American History",
          "q": "What are two ways that Americans can participate in their democracy?",
          "a": (
              "Vote, join a political party, help with a campaign, join a civic"
              " group, join a community group, give an elected official your"
              " opinion on an issue, call Senators and Representatives,"
              " publicly support or oppose an issue or policy, run for office,"
              " write to a newspaper"
          ),
      },
      {
          "category": "American History",
          "q": "When is the last day you can send in federal income tax forms?",
          "a": "April 15",
      },
      {
          "category": "American History",
          "q": "When must all men register for the Selective Service?",
          "a": "At age eighteen (18) and up to age twenty-six (26)",
      },
      {
          "category": "American History",
          "q": "What is one reason colonists came to America?",
          "a": "Freedom, political liberty, religious freedom, economic opportunity",
      },
      {
          "category": "American History",
          "q": "Who lived in America before the Europeans arrived?",
          "a": "American Indians / Native Americans",
      },
      {
          "category": "American History",
          "q": "What group of people was taken to America and sold as slaves?",
          "a": "Africans / People from Africa",
      },
      {
          "category": "American History",
          "q": "Why did the colonists fight the British?",
          "a": (
              "Because of high taxes (taxation without representation), because"
              " the British army stayed in their houses, because they didn't"
              " have self-government"
          ),
      },
      {
          "category": "American History",
          "q": "Who wrote the Declaration of Independence?",
          "a": "Thomas Jefferson",
      },
      {
          "category": "American History",
          "q": "When was the Declaration of Independence adopted?",
          "a": "July 4, 1776",
      },
      {
          "category": "American History",
          "q": "There were 13 original states. Name three.",
          "a": (
              "New Hampshire, Massachusetts, Rhode Island, Connecticut, New"
              " York, New Jersey, Pennsylvania, Delaware, Maryland, Virginia,"
              " North Carolina, South Carolina, Georgia"
          ),
      },
      {
          "category": "American History",
          "q": "What happened at the Constitutional Convention?",
          "a": (
              "The Constitution was written, the Founding Fathers wrote the"
              " Constitution"
          ),
      },
      {
          "category": "American History",
          "q": "When was the Constitution written?",
          "a": "1787",
      },
      {
          "category": "American History",
          "q": "The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.",
          "a": "James Madison, Alexander Hamilton, John Jay, Publius",
      },
      {
          "category": "American History",
          "q": "What is one thing Benjamin Franklin is famous for?",
          "a": (
              "U.S. diplomat, oldest member of the Constitutional Convention,"
              " first Postmaster General of the United States, writer of"
              " 'Poor Richard's Almanack', started the first free libraries"
          ),
      },
      {
          "category": "American History",
          "q": "Who is the 'Father of Our Country'?",
          "a": "George Washington",
      },
      {
          "category": "American History",
          "q": "Who was the first President?",
          "a": "George Washington",
      },
      # 1800s & Recent History
      {
          "category": "American History",
          "q": "What territory did the United States buy from France in 1803?",
          "a": "The Louisiana Territory / Louisiana",
      },
      {
          "category": "American History",
          "q": "Name one war fought by the U.S. in the 1800s.",
          "a": (
              "War of 1812, Mexican-American War, Civil War, Spanish-American"
              " War"
          ),
      },
      {
          "category": "American History",
          "q": "Name the U.S. war between the North and the South.",
          "a": "The Civil War / The War between the States",
      },
      {
          "category": "American History",
          "q": "Name one problem that led to the Civil War.",
          "a": "Slavery, economic reasons, states' rights",
      },
      {
          "category": "American History",
          "q": "What was one important thing that Abraham Lincoln did?",
          "a": (
              "Freed the slaves (Emancipation Proclamation), saved (or"
              " preserved) the Union, led the United States during the Civil"
              " War"
          ),
      },
      {
          "category": "American History",
          "q": "What did the Emancipation Proclamation do?",
          "a": (
              "Freed the slaves, freed slaves in the Confederacy, freed slaves"
              " in the Southern states"
          ),
      },
      {
          "category": "American History",
          "q": "What did Susan B. Anthony do?",
          "a": "Fought for women's rights, fought for civil rights",
      },
      {
          "category": "American History",
          "q": "Name one war fought by the United States in the 1900s.",
          "a": (
              "World War I, World War II, Korean War, Vietnam War, Persian"
              " Gulf War"
          ),
      },
      {
          "category": "American History",
          "q": "Who was President during World War I?",
          "a": "Woodrow Wilson",
      },
      {
          "category": "American History",
          "q": "Who was President during the Great Depression and World War II?",
          "a": "Franklin D. Roosevelt",
      },
      {
          "category": "American History",
          "q": "Who did the United States fight in World War II?",
          "a": "Japan, Germany, and Italy",
      },
      {
          "category": "American History",
          "q": "Before he was President, Eisenhower was a general. What war was he in?",
          "a": "World War II",
      },
      {
          "category": "American History",
          "q": "During the Cold War, what was the main concern of the United States?",
          "a": "Communism",
      },
      {
          "category": "American History",
          "q": "What movement tried to end racial discrimination?",
          "a": "Civil rights movement",
      },
      {
          "category": "American History",
          "q": "What did Martin Luther King, Jr. do?",
          "a": (
              "Fought for civil rights, worked for equality for all Americans"
          ),
      },
      {
          "category": "American History",
          "q": "What major event happened on September 11, 2001, in the U.S.?",
          "a": "Terrorists attacked the United States",
      },
      {
          "category": "American History",
          "q": "Name one American Indian tribe in the United States.",
          "a": (
              "Cherokee, Navajo, Sioux, Chippewa, Choctaw, Pueblo, Apache,"
              " Iroquois, Creek, Blackfeet, Seminole, Cheyenne, Arawak,"
              " Mohegan, Huron, Oneida, Lakota, Crow, Hopi, Inuit"
          ),
      },
      # Integrated Civics - Geography & Symbols
      {
          "category": "Integrated Civics",
          "q": "Name one of the two longest rivers in the United States.",
          "a": "Missouri (River) or Mississippi (River)",
      },
      {
          "category": "Integrated Civics",
          "q": "What ocean is on the West Coast of the United States?",
          "a": "Pacific Ocean",
      },
      {
          "category": "Integrated Civics",
          "q": "What ocean is on the East Coast of the United States?",
          "a": "Atlantic Ocean",
      },
      {
          "category": "Integrated Civics",
          "q": "Name one U.S. territory.",
          "a": (
              "Puerto Rico, U.S. Virgin Islands, American Samoa, Northern"
              " Mariana Islands, Guam"
          ),
      },
      {
          "category": "Integrated Civics",
          "q": "Name one state that borders Canada.",
          "a": (
              "Maine, New Hampshire, Vermont, New York, Pennsylvania, Ohio,"
              " Michigan, Minnesota, North Dakota, Montana, Idaho, Washington,"
              " Alaska"
          ),
      },
      {
          "category": "Integrated Civics",
          "q": "Name one state that borders Mexico.",
          "a": "California, Arizona, New Mexico, Texas",
      },
      {
          "category": "Integrated Civics",
          "q": "What is the capital of the United States?",
          "a": "Washington, D.C.",
      },
      {
          "category": "Integrated Civics",
          "q": "Where is the Statue of Liberty?",
          "a": "New York Harbor (Liberty Island), New Jersey, near New York City",
      },
      {
          "category": "Integrated Civics",
          "q": "Why does the flag have 13 stripes?",
          "a": (
              "Because there were 13 original colonies, because the stripes"
              " represent the original colonies"
          ),
      },
      {
          "category": "Integrated Civics",
          "q": "Why does the flag have 50 stars?",
          "a": (
              "Because there is one star for each state, because each star"
              " represents a state, because there are 50 states"
          ),
      },
      {
          "category": "Integrated Civics",
          "q": "What is the name of the national anthem?",
          "a": "The Star-Spangled Banner",
      },
      {
          "category": "Integrated Civics",
          "q": "When do we celebrate Independence Day?",
          "a": "July 4",
      },
      {
          "category": "Integrated Civics",
          "q": "Name two national U.S. holidays.",
          "a": (
              "New Year's Day, Martin Luther King, Jr. Day, Presidents' Day,"
              " Memorial Day, Juneteenth, Independence Day, Labor Day,"
              " Columbus Day, Veterans Day, Thanksgiving Day, Christmas Day"
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
          f"**Read this sentence aloud clearly:**\n\n> `{st.session_state.active_read}`"
      )

  with col_write:
    st.subheader("✍️ Writing Practice & Dictation Checker")
    writing_pool = [
        "Abraham Lincoln was the president during the Civil War.",
        "The American flag has red, white, and blue stripes.",
        "Citizens vote for the President in November.",
        "George Washington is the father of our country.",
        "Capitalism is the economic system of the United States.",
    ]
    
    if st.button("Get Dictation Prompt Audio"):
      st.session_state.active_write = random.choice(writing_pool)

    if "active_write" in st.session_state:
      st.info("🔊 **Audio Prompt Loaded:** Click the play button below to listen to the officer's dictation.")

      # Browser text-to-speech audio trigger widget
      text_to_speak = st.session_state.active_write.replace("'", "\\'")
      audio_html = f"""
            <div style="margin: 10px 0;">
                <button onclick="speakText()" style="background-color: #2e7d32; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 14px;">
                    ▶️ Play Audio Dictation
                </button>
            </div>
            <script>
                function speakText() {{
                    if ('speechSynthesis' in window) {{
                        window.speechSynthesis.cancel();
                        var utterance = new SpeechSynthesisUtterance('{text_to_speak}');
                        utterance.rate = 0.9; // Slow down slightly for clarity
                        utterance.pitch = 1.0;
                        window.speechSynthesis.speak(utterance);
                    }} else {{
                        alert('Sorry, your browser does not support text-to-speech audio.');
                    }}
                }}
            </script>
            """
      components.html(audio_html, height=60)

      user_writing = st.text_input("Type the sentence you heard word-for-word:")
      if st.button("Evaluate Writing"):
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
