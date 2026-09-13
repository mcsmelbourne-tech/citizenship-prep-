import random
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="US Citizenship Test Prep", page_icon=Payal-", layout="wide"
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

# Sidebar Navigation Tabs (Added new vocabulary & sentence builder tab)
tabs = st.tabs([
    "📋 N-400 & Interview Vocabulary",
    "📚 Vocabulary & Sentence Builder",
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
    st.subheader("📚 Detailed N-400 Terms & Definitions")
    vocab_detailed_data = {
        "General Application": {
            "Habitually": {
                "meaning": "Often or repeatedly, as a regular pattern or habit.",
                "context": "Used in questions about alcohol consumption, support of dependents, or general conduct.",
                "officer_tip": "Be completely honest if asked about habits. Inconsistency with your written form can cause delays."
            },
            "Verify": {
                "meaning": "To prove, check, or establish that something is true, accurate, or correct.",
                "context": "Refers to reviewing documents, tax papers, or personal data entries.",
                "officer_tip": "Bring original copies of all identity and tax documents to the interview to verify instantly."
            },
            "Registered": {
                "meaning": "Signed up officially with a government body or official database.",
                "context": "Relates to selective service registration, voting rolls, or state registries.",
                "officer_tip": "Men aged 18-25 must show proof of Selective Service registration."
            },
        },
        "Family & Status": {
            "Marital Status": {
                "meaning": "Your current legal standing regarding marriage (single, married, divorced, or widowed).",
                "context": "Determines whether you file under the 3-year or 5-year permanent resident rule.",
                "officer_tip": "Bring marriage certificates, divorce decrees, or death certificates of past spouses."
            },
            "Spouse": {
                "meaning": "Your legally recognized husband or wife.",
                "context": "Core to evaluating joint tax returns, residency timelines, and family petitions.",
                "officer_tip": "If your spouse is a U.S. citizen, be prepared to answer questions about their background too."
            },
            "Dependent": {
                "meaning": "Someone who relies on you primarily for financial support, such as a minor child or relative.",
                "context": "Used when reviewing household members, child support obligations, and tax exemptions.",
                "officer_tip": "Keep records of child support payments if you have children from a previous relationship."
            },
        },
        "Legal & Proceedings": {
            "Swear": {
                "meaning": "To make a solemn, formal promise under oath, invoking truthfulness.",
                "context": "Done right at the beginning of your interview before answering any questions.",
                "officer_tip": "Understand that lying after swearing an oath constitutes perjury under federal law."
            },
            "Citation": {
                "meaning": "An official written notice, warning, or ticket issued by law enforcement (e.g., traffic violations).",
                "context": "Appears in Part 10 of the N-400 regarding arrests, detentions, and traffic tickets.",
                "officer_tip": "Minor traffic tickets under $500 usually don't block citizenship, but failing to disclose them will."
            },
            "Affiliation": {
                "meaning": "A formal connection, membership, or association with a club, group, or organization.",
                "context": "Scrutinizes past or present ties to political parties, community groups, or ideological associations.",
                "officer_tip": "Review all professional and social organizations you belong to before the interview."
            },
        }
    }
    selected_category = st.selectbox(
        "Select Vocabulary Category:", list(vocab_detailed_data.keys()), key="vocab_cat"
    )
    
    category_words = vocab_detailed_data[selected_category]
    selected_vocab = st.selectbox(
        "Select a vocabulary word to review:", list(category_words.keys()), key="vocab_word"
    )
    
    word_info = category_words[selected_vocab]
    st.info(f"**Meaning:** {word_info['meaning']}")
    st.markdown(f"**Application Context:** {word_info['context']}")
    st.warning(f"💡 **Officer Tip:** {word_info['officer_tip']}")
  with col2:
    st.subheader("⚠️ Common Background Risk Areas")
    st.markdown("Select a risk area below to deep-dive into what USCIS checks and how to prepare:")
    
    risk_detailed_dict = {
        "Taxes": {
            "question": "Have you ever failed to file a federal, state, or local tax return since you became a lawful permanent resident?",
            "risk_level": "High Risk",
            "pitfalls": "Omission of state returns, unfiled years due to low income, or failure to pay agreed-upon tax arrears.",
            "action_plan": "Pull official IRS tax transcripts for the last 3-5 years. If on a payment plan with the IRS, bring proof of regular payments."
        },
        "Organizations": {
            "question": "Have you ever been a member of, or associated with, any terrorist group, communist party, totalitarian organization, or militia?",
            "risk_level": "Critical Risk",
            "pitfalls": "Inadvertent membership in mandatory civic groups in home countries that held political affiliations.",
            "action_plan": "Consult an immigration attorney immediately if you had any historical affiliations with governmental or political mass organizations."
        },
        "Lie / Misrepresentation": {
            "question": "Have you ever given any false, fraudulent, or misleading information to a U.S. government official to gain entry or benefits?",
            "risk_level": "Severe Risk",
            "pitfalls": "Discrepancies between historical visa applications and your current N-400 disclosures.",
            "action_plan": "Disclose and clarify historical record discrepancies upfront with supporting documentation or legal counsel."
        },
        "Removal Proceedings": {
            "question": "Have you ever been placed in removal, exclusion, rescission, or deportation proceedings?",
            "risk_level": "High Risk",
            "pitfalls": "Failing to disclose past border administrative actions, expedited removals, or old immigration court notices.",
            "action_plan": "Obtain your complete A-file (Alien File) via FOIA requests to ensure all past immigration history is fully transparent."
        }
    }
    selected_risk = st.selectbox("Select Background Risk Area:", list(risk_detailed_dict.keys()), key="risk_area")
    risk_data = risk_detailed_dict[selected_risk]
    
    st.error(f"**Official Question:** `{risk_data['question']}`")
    st.markdown(f"**Risk Level:** **{risk_data['risk_level']}**")
    st.markdown(f"**Common Pitfalls:** {risk_data['pitfalls']}")
    st.success(f"🛡️ **Preparation Strategy:** {risk_data['action_plan']}")

# ---------------------------------------------------------
# TAB 2: Vocabulary & Sentence Builder (New Tab requested)
# ---------------------------------------------------------
with tabs[1]:
  st.header("Comprehensive Vocabulary & Sentence Builder")
  st.markdown("Select a thematic category, choose a vocabulary word, and review three contextual sentences built for each term[cite: 7].")

  master_vocab_dict = {
      "PEOPLE": {
          "Adams": [
              "John Adams was the second President of the United States.",
              "Adams played a vital role in drafting the Declaration of Independence.",
              "Many historians study the letters exchanged between Adams and his wife Abigail."
          ],
          "Lincoln": [
              "Abraham Lincoln issued the Emancipation Proclamation during the Civil War.",
              "Lincoln is remembered as one of the greatest American presidents.",
              "The Lincoln Memorial stands proudly in Washington, D.C."
          ],
          "Washington": [
              "George Washington was commander-in-chief of the Continental Army.",
              "Washington became the first President of the United States.",
              "The capital city of the nation is named after Washington."
          ]
      },
      "CIVICS": {
          "American Indians": [
              "American Indians lived in North America before the Europeans arrived.",
              "Many different American Indians tribes have rich cultural traditions.",
              "The history of American Indians is an integral part of U.S. heritage."
          ],
          "capital": [
              "Washington, D.C. is the capital of the United States.",
              "Every state in the country has its own designated capital city.",
              "Lawmakers meet at the capital building to pass new legislation."
          ],
          "citizens": [
              "U.S. citizens have both important rights and unique responsibilities.",
              "Naturalized citizens enjoy the same protections under the law.",
              "All citizens aged eighteen and older have the right to vote."
          ],
          "Civil War": [
              "The Civil War was fought between the North and the South.",
              "Slavery was a major issue that led directly to the Civil War.",
              "President Abraham Lincoln led the nation through the Civil War."
          ],
          "Congress": [
              "Congress makes federal laws for the United States.",
              "Congress consists of the Senate and the House of Representatives.",
              "Members of Congress meet regularly in Washington, D.C."
          ],
          "Father of Our Country": [
              "George Washington is commonly known as the Father of Our Country.",
              "Schools teach children about the legacy of the Father of Our Country.",
              "The Father of Our Country led the American colonies to independence."
          ],
          "flag": [
              "The American flag has thirteen stripes for the original colonies.",
              "The flag features fifty stars representing the fifty states.",
              "Citizens show loyalty to the country when they salute the flag."
          ],
          "free": [
              "The Declaration of Independence stated that the United States is free.",
              "Colonists fought to live in a free and independent nation.",
              "Citizens enjoy free speech guaranteed by the Constitution."
          ],
          "freedom of speech": [
              "Freedom of speech is protected by the First Amendment.",
              "Citizens can express their political opinions through freedom of speech.",
              "Freedom of speech allows people to debate public issues openly."
          ],
          "President": [
              "The President is in charge of the executive branch.",
              "We elect a President every four years in November.",
              "The President signs bills to make them official laws."
          ],
          "right": [
              "Voting in a federal election is a right reserved for citizens.",
              "The Constitution protects the basic right of religious freedom.",
              "Every person has the right to a fair trial."
          ],
          "Senators": [
              "There are one hundred U.S. Senators in Congress.",
              "Each state elects two Senators to represent them.",
              "We elect a U.S. Senator for a term of six years."
          ],
          "state/states": [
              "The United States is made up of fifty individual states.",
              "Each state has its own government and capital city.",
              "Powers not given to the federal government belong to the states."
          ],
          "White House": [
              "The President lives and works in the White House.",
              "The White House is located in Washington, D.C.",
              "Many tourists visit Washington, D.C., to see the White House."
          ]
      },
      "PLACES": {
          "Alaska": [
              "Alaska is the largest state in the United States by area.",
              "Alaska shares a border with Canada to its east.",
              "Many people visit Alaska to see its vast wilderness."
          ],
          "California": [
              "California is a major state located on the West Coast.",
              "California shares a southern international border with Mexico.",
              "Millions of people live and work across California."
          ],
          "Canada": [
              "Canada is a country located directly north of the United States.",
              "Many northern U.S. states share a long border with Canada.",
              "Trade between the United States and Canada is very active."
          ],
          "Delaware": [
              "Delaware was one of the thirteen original states.",
              "Delaware is located on the East Coast of the United States.",
              "The state of Delaware ratified the Constitution early on."
          ],
          "Mexico": [
              "Mexico is located directly south of the United States.",
              "Several American states share a border with Mexico.",
              "Cultural ties between the United States and Mexico are very strong."
          ],
          "New York City": [
              "New York City is the largest city in the state of New York.",
              "The Statue of Liberty stands near New York City.",
              "Many immigrants arrived through New York City historically."
          ],
          "United States": [
              "The United States is a constitutional republic.",
              "People come from all over the world to live in the United States.",
              "The economic system of the United States is a capitalist market."
          ],
          "Washington": [
              "Washington is a state located in the Pacific Northwest.",
              "The state of Washington borders Canada to the north.",
              "Washington is known for its beautiful mountains and coastlines."
          ],
          "Washington, D.C.": [
              "Washington, D.C. is the federal capital of the country.",
              "The federal government operates out of Washington, D.C.",
              "Major monuments and museums are located in Washington, D.C."
          ]
      },
      "MONTHS": {
          "February": [
              "Presidents' Day is celebrated in the month of February.",
              "February is traditionally the shortest month of the year.",
              "Schools often hold historical events throughout February."
          ],
          "May": [
              "Memorial Day is observed on the last Monday of May.",
              "Spring weather is usually pleasant during the month of May.",
              "Many community events take place in May."
          ],
          "June": [
              "Flag Day is celebrated annually on June fourteenth.",
              "June marks the official beginning of the summer season.",
              "Many families plan vacations during the month of June."
          ],
          "July": [
              "Independence Day is celebrated nationwide on July fourth.",
              "July is typically a warm summer month in the United States.",
              "Fireworks light up the sky every July."
          ],
          "September": [
              "Labor Day is celebrated on the first Monday of September.",
              "September marks the beginning of the autumn season.",
              "Schools reopen for classes during September."
          ],
          "October": [
              "Columbus Day is observed on the second Monday of October.",
              "The leaves change colors during October.",
              "Fall festivals are common throughout October."
          ],
          "November": [
              "Americans vote for the President in November.",
              "Thanksgiving is celebrated on the fourth Thursday of November.",
              "The weather becomes colder during November."
          ]
      },
      "HOLIDAYS": {
          "Presidents’ Day": [
              "Presidents' Day honors past leaders like Washington and Lincoln.",
              "Banks and government offices close on Presidents' Day.",
              "Presidents' Day takes place in February."
          ],
          "Memorial Day": [
              "Memorial Day honors soldiers who died while serving in the military.",
              "Many people attend parades on Memorial Day.",
              "Memorial Day is observed in late May."
          ],
          "Flag Day": [
              "Flag Day commemorates the adoption of the American flag.",
              "Citizens display the flag proudly on Flag Day.",
              "Flag Day is celebrated on June fourteenth."
          ],
          "Independence Day": [
              "Independence Day celebrates the adoption of the Declaration of Independence.",
              "Communities host parades and fireworks on Independence Day.",
              "Independence Day falls on July fourth."
          ],
          "Labor Day": [
              "Labor Day honors the American worker and labor movement.",
              "Labor Day marks the unofficial end of summer.",
              "Parades and picnics are popular on Labor Day."
          ],
          "Columbus Day": [
              "Columbus Day commemorates Christopher Columbus's arrival in the Americas.",
              "Some regions observe Indigenous Peoples' Day alongside Columbus Day.",
              "Columbus Day takes place in October."
          ],
          "Thanksgiving": [
              "Thanksgiving is a traditional holiday for family gatherings.",
              "People give thanks for their blessings on Thanksgiving.",
              "Roast turkey is a traditional meal served on Thanksgiving."
          ]
      },
      "VERBS": {
          "can": [
              "Citizens can vote in federal elections once they turn eighteen.",
              "Anyone can practice their chosen religion freely.",
              "You can study civics questions online."
          ],
          "come": [
              "Early colonists chose to come to America for freedom.",
              "People come to the United States seeking economic opportunities.",
              "Citizens come together to participate in democracy."
          ],
          "elect": [
              "Voters elect members of Congress every few years.",
              "We elect a President to serve a four-year term.",
              "Citizens have the power to elect local and national leaders."
          ],
          "have/has": [
              "The United States has fifty individual states.",
              "Every state has two Senators representing them in Congress.",
              "The American flag has red, white, and blue stripes."
          ],
          "is/was/be": [
              "George Washington was the first President of the United States.",
              "The Constitution is the supreme law of the land.",
              "It is important to study for the naturalization test."
          ],
          "lives/lived": [
              "American Indians lived in North America for thousands of years.",
              "The President lives in the White House during their term.",
              "Millions of people live across the fifty states."
          ],
          "meets": [
              "Congress meets in the Capitol building to make laws.",
              "The Supreme Court meets to review constitutional questions.",
              "The President's Cabinet meets to offer advice."
          ],
          "pay": [
              "Citizens must pay federal income taxes by April fifteenth.",
              "Taxpayers pay local and state taxes to fund public services.",
              "Citizens do not have to pay a poll tax to vote."
          ],
          "vote": [
              "Eligible citizens can vote in local and federal elections.",
              "People vote for the President in November.",
              "Exercising your right to vote strengthens democracy."
          ],
          "want": [
              "Many colonists wanted freedom from British rule.",
              "People want to build a better life in America.",
              "Voters want their elected officials to listen to their concerns."
          ]
      },
      "OTHER (FUNCTION)": {
          "and": [
              "The legislative, executive, and judicial branches share power.",
              "The flag features red, white, and blue colors.",
              "Citizens have both rights and responsibilities."
          ],
          "during": [
              "Lincoln led the nation during the Civil War.",
              "President Roosevelt served during World War II.",
              "Citizens should remain informed during elections."
          ],
          "for": [
              "We elect a President for a term of four years.",
              "Colonists fought for their independence from Great Britain.",
              "People study hard for the citizenship test."
          ],
          "here": [
              "Many diverse communities thrive here in the United States.",
              "Immigrants start new lives here.",
              "Study materials are provided right here for your convenience."
          ],
          "in": [
              "The Constitution was written in 1787.",
              "Elections for president take place in November.",
              "There are fifty states in the country."
          ],
          "of": [
              "The Constitution is the supreme law of the land.",
              "Thomas Jefferson wrote the Declaration of Independence.",
              "The capital of the United States is Washington, D.C."
          ],
          "on": [
              "Independence Day is celebrated on July fourth.",
              "Tax returns are due on April fifteenth.",
              "Supreme Court justices make decisions on major cases."
          ],
          "the": [
              "The President signs bills to become laws.",
              "The Supreme Court is the highest court in the land.",
              "The American flag represents the nation."
          ],
          "to": [
              "Everyone must obey the law.",
              "Immigrants pledge loyalty to the United States.",
              "Citizens have the right to vote in elections."
          ],
          "we": [
              "We elect our leaders through democratic elections.",
              "We show loyalty to the flag when reciting the pledge.",
              "We the People established the Constitution."
          ]
      },
      "OTHER (CONTENT)": {
          "blue": [
              "The American flag contains stripes of red, white, and blue.",
              "The blue field on the flag holds fifty white stars.",
              "The national colors include red, white, and blue."
          ],
          "dollar bill": [
              "Famous American presidents are pictured on paper currency and the dollar bill.",
              "George Washington's portrait appears on the one-dollar bill.",
              "Financial transactions involve coins and the dollar bill."
          ],
          "fifty/50": [
              "There are fifty states in the United States.",
              "The flag has fifty stars to represent each state.",
              "Fifty members represent the states in various capacities."
          ],
          "first": [
              "George Washington was the first President of the United States.",
              "The first ten amendments are called the Bill of Rights.",
              "Labor Day falls on the first Monday of September."
          ],
          "largest": [
              "Alaska is the largest state by geographical area.",
              "The country contains some of the largest rivers in the world.",
              "California is among the largest states by population."
          ],
          "most": [
              "Most states have two representatives in the Senate.",
              "Most citizens participate in national elections.",
              "History tests cover most of these foundational topics."
          ],
          "north": [
              "Canada is located directly north of the United States.",
              "The Northern states fought during the Civil War.",
              "Compass directions point north toward the pole."
          ],
          "one": [
              "The Constitution is the supreme law, and no one is above it.",
              "There is one President leading the executive branch.",
              "Every citizen has one vote in an election."
          ],
          "one hundred/100": [
              "There are one hundred Senators in the U.S. Senate.",
              "Each state contributes to that total of one hundred senators.",
              "Civics tests sample from a pool of one hundred official questions."
          ],
          "people": [
              "We the People established the U.S. Constitution.",
              "A democracy empowers the people to choose their leaders.",
              "People from all over the world immigrate to America."
          ],
          "red": [
              "The American flag features red and white stripes.",
              "Red is one of the three primary national colors.",
              "Red stripes stand alongside white and blue on the banner."
          ],
          "second": [
              "John Adams was the second President.",
              "Columbus Day is observed on the second Monday of October.",
              "Reviewing material a second time helps with memory."
          ],
          "south": [
              "Mexico borders the United States to the south.",
              "Southern states formed a confederacy during the Civil War.",
              "Warm weather is common in the south."
          ],
          "taxes": [
              "Citizens must file and pay federal income taxes.",
              "Colonists fought the British partly because of unfair taxes.",
              "Local governments use taxes to fund public schools and roads."
          ],
          "white": [
              "The American flag features white stars and stripes.",
              "The White House is the official residence of the President.",
              "White is paired with red and blue on the national flag."
          ]
      }
  }

  selected_cat = st.selectbox("Select Category:", list(master_vocab_dict.keys()), key="master_cat")
  word_options = list(master_vocab_dict[selected_cat].keys())
  selected_word = st.selectbox("Select Word:", word_options, key="master_word")

  st.markdown(f"### Sentences for **{selected_word}**:")
  sentences = master_vocab_dict[selected_cat][selected_word]
  for idx, sentence in enumerate(sentences, 1):
      st.markdown(f"* **Sentence {idx}:** {sentence}")

# ---------------------------------------------------------
# TAB 3: Expanded Civics Question Bank (Full Official Pool)
# ---------------------------------------------------------
with tabs[2]:
  st.header("Civics Question Bank (Principles & History)")
  st.markdown(
      "Practice questions spanning American Government, American History, and"
      " Integrated Civics."
  )
  
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
          "a": "Check current office holder",
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

  selected_cat_civics = st.selectbox(
      "Filter by Category:",
      ["All"] + list(set([item["category"] for item in civics_bank])),
  )
  filtered_bank = (
      civics_bank
      if selected_cat_civics == "All"
      else [item for item in civics_bank if item["category"] == selected_cat_civics]
  )
  q_idx = st.selectbox(
      "Select a question:",
      options=range(len(filtered_bank)),
      format_func=lambda x: filtered_bank[x]["q"],
  )
  if st.button("Show Answer"):
    st.success(f"**Correct Answer:** {filtered_bank[q_idx]['a']}")

# ---------------------------------------------------------
# TAB 4: English Reading & Writing Skill Practice
# ---------------------------------------------------------
with tabs[3]:
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
                        utterance.rate = 0.9;
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
# TAB 5: Mock Test Simulator (15 Questions)
# ---------------------------------------------------------
with tabs[4]:
  st.header("Full Interview & Test Simulator (15 Questions)")
  st.markdown(
      "Simulate the actual testing environment. You will be tested on **15 random civics"
      " questions**. Answer as many as you can accurately!"
  )
  if st.button("Start 15-Question Simulation Test"):
    st.session_state.sim_questions = random.sample(
        civics_bank, min(15, len(civics_bank))
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
      submitted = st.form_submit_button("Submit All 15 Answers")
      if submitted:
        st.subheader("Simulation Results & Scorecard")
        for i, item in enumerate(st.session_state.sim_questions):
          st.write(f"**Q{i+1}:** {item['q']}")
          st.write(f"Your input: `{user_answers[i]}`")
          st.info(f"Official Answer Key: {item['a']}")
          st.divider()
