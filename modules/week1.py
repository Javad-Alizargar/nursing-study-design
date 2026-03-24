import streamlit as st

def render_part_1():
    st.header("📖 Part 1: The 7 Steps to the Perfect PICO Search")
    st.info("Review the materials below. You will apply these concepts in the Interactive Sandbox (Part 2) and the Knowledge Check (Part 3).")

    st.subheader("What is Evidence-Based Nursing Practice?")
    st.write("> *\"Evidence-based practice in nursing is using and carrying out nursing practices based on the best available knowledge. Evidence-based practice integrates the nurse’s clinical expertise with the best external research evidence, and takes into account patient preferences to deliver quality nursing care.\"*")
    st.divider()

    st.subheader("The 7-Step Search Strategy")
    col_steps1, col_steps2 = st.columns(2)
    with col_steps1:
        st.markdown("""
        **1. Formulate the PICO Question:** Identify the Patient/Problem, Intervention, Comparison, and Outcome.
        **2. Identify Keywords:** Break down each PICO element into searchable terms.
        **3. Plan Search Strategy:** Translate natural language to database subject descriptors and find synonyms.
        **4. Execute the Search:** Use Boolean operators (AND/OR) to combine your keyword searches.
        """)
    with col_steps2:
        st.markdown("""
        **5. Refine Results:** Apply limiters like Date, Publication Type, and Evidence-Based Practice.
        **6. Review Literature:** Select the most relevant articles for your clinical question.
        **7. Assess the Evidence:** Determine the strength and level of the evidence you found.
        """)
    st.divider()

    with st.expander("🩺 Clinical Scenario & Keyword Mapping: Post-Operative Ileus", expanded=True):
        st.write("**The Situation:** A 55-year-old man recovering from a laparoscopic prostatectomy complains of abdominal pain and nausea. His abdomen is distended with no bowel sounds. The physician diagnoses a paralytic ileus. The nursing committee wants to know if chewing gum post-operatively can prevent this.")
        st.markdown("**The PICO Breakdown & Keywords:**")
        pico_data = {
            "PICO Element": ["P (Patient/Population)", "I (Intervention)", "C (Comparison)", "O (Outcome)"],
            "Clinical Terms": ["Patients undergoing abdominal surgery", "Chewing gum", "Not chewing gum", "Affects post-operative ileus"],
            "Search Synonyms (Use 'OR')": ["Abdominal surgery OR Surgery OR Postoperative OR Recovery", "Chewing Gum OR Gum", "Not chewing gum", "Postoperative Ileus OR Paralytic Ileus OR Ileus"]
        }
        st.table(pico_data)
        st.info("**Final Clinical Question:** *In patients undergoing abdominal surgery, is there evidence to suggest that chewing gum post-operatively compared with not chewing gum post-operatively affects post-operative ileus?*")
    st.divider()

    st.subheader("Assessing the Evidence: The Hierarchy")
    st.write("When reviewing your search results (Step 7), prioritize studies at the top of this hierarchy:")
    st.markdown("""
    | Level | Study Design | Definition |
    | :--- | :--- | :--- |
    | **1 (Highest)** | **Meta-Analysis** | A systematic review that uses quantitative methods to synthesize & summarize results. |
    | **2** | **Systematic Review** | A summary of medical literature using explicit methods for comprehensive search & critical appraisal. |
    | **3** | **Randomized Controlled Trial (RCT)** | Participants are randomly allocated into experimental or control groups. |
    | **4** | **Cohort Study** | Identifies participants with a condition/treatment and follows them over time. |
    | **5** | **Case Control Study** | Identifies participants with an outcome (cases) & without (controls) and looks backward. |
    | **6 (Lowest)** | **Case Report/Series** | A report on one or more participants with a particular outcome. |
    """)

def render_part_2():
    st.header("🛠️ Part 2: Interactive Sandbox")
    st.write("Apply the 7-Step strategy and PICO logic to new clinical scenarios.")

    # --- Interactive Exercise 1: PICO Builder ---
    st.subheader("Exercise 1: Construct the PICO")
    st.write("> **Scenario:** As a school nurse in a local high school, you notice an increase in teens that are vaping. You’d like to provide students with factual educational materials to help them stop or reduce their smoking.")
    
    st.markdown("**Select the correct components to build your clinical question:**")
    col1, col2 = st.columns(2)
    with col1:
        p_guess = st.selectbox("P (Patient/Problem)", ["Select...", "School nurses", "Teens who vape", "Local high schools"])
        i_guess = st.selectbox("I (Intervention)", ["Select...", "Factual education materials", "Vaping", "Reducing smoking"])
    with col2:
        c_guess = st.selectbox("C (Comparison)", ["Select...", "Adult smokers", "Vaping", "No education/Standard care"])
        o_guess = st.selectbox("O (Outcome)", ["Select...", "Reduction in vaping", "Becoming a nurse", "High school graduation"])

    if p_guess != "Select..." and i_guess != "Select..." and c_guess != "Select..." and o_guess != "Select...":
        if p_guess == "Teens who vape" and i_guess == "Factual education materials" and c_guess == "No education/Standard care" and o_guess == "Reduction in vaping":
            st.success("✅ **Perfect! Your clinical question is:**")
            st.info(f"**In {p_guess.lower()}, does {i_guess.lower()} compared to {c_guess.lower()} result in a {o_guess.lower()}?**")
        else:
            st.warning("Not quite right. Review the scenario and try adjusting your selections.")

    st.divider()

    # --- Interactive Exercise 2: Boolean Search Simulator ---
    st.subheader("Exercise 2: The Boolean Database Simulator")
    st.write("Now that you have your PICO, let's execute Step 4 of the EBP Search. See how Boolean operators change the number of articles returned in our mock database.")
    
    term1 = st.checkbox("Search Term 1: 'Vaping'")
    term2 = st.checkbox("Search Term 2: 'Teens'")
    operator = st.radio("Combine terms with:", ["AND (Intersection)", "OR (Union)"], horizontal=True)
    
    results = 0
    if term1 and term2:
        if "AND" in operator:
            results = 145  # Narrows the search
            st.success("🎯 **Highly Specific:** You found articles mentioning BOTH vaping and teens.")
        else:
            results = 18450 # Broadens the search
            st.warning("🌊 **Too Broad:** You found every article about vaping PLUS every article about teens.")
    elif term1:
        results = 8500
    elif term2:
        results = 10200
        
    st.metric(label="Articles Found", value=f"{results:,}")

    st.divider()

    # --- Interactive Exercise 3: Study Design Selection ---
    st.subheader("Exercise 3: Select the Study Design")
    st.write("To truly prove your educational materials cause a reduction in vaping (Level 2 Evidence), which study design must you attempt to set up?")
    
    design_choice = st.radio("Choose the Gold Standard design for this intervention:", 
                             ["Cross-Sectional Survey", "Case-Control Study", "Randomized Controlled Trial (RCT)", "Case Report"],
                             index=None)
    
    if design_choice == "Randomized Controlled Trial (RCT)":
        st.success("🏆 **Correct!** An RCT is the highest level of primary experimental evidence to prove an intervention works.")
    elif design_choice is not None:
        st.error("Incorrect. Remember, if you are testing an **Intervention** (doing something to the patient), you need an experimental design.")

def render_part_3():
    st.header("📝 Part 3: Knowledge Check")
    st.write("Test your understanding of Week 1 concepts. Select the best answer for each question.")

    with st.form("quiz_form"):
        st.subheader("Question 1")
        q1 = st.radio("In the PICO framework, what does the 'C' stand for?",
                      ["Cohort", "Control", "Comparison", "Context"], 
                      index=None)

        st.subheader("Question 2")
        q2 = st.radio("Which study design is considered the 'Gold Standard' for testing the effectiveness of a new nursing intervention?",
                      ["Cross-Sectional Survey", "Randomized Controlled Trial (RCT)", "Case-Control Study", "Cohort Study"], 
                      index=None)

        st.subheader("Question 3")
        q3 = st.radio("If you want to understand the long-term health effects of vaping by following a healthy group of high schoolers over the next 10 years, which design are you using?",
                      ["Meta-Analysis", "Case Report", "Cohort Study", "Systematic Review"], 
                      index=None)

        # --- NEW QUESTIONS ADDED HERE ---
        st.subheader("Question 4")
        q4 = st.radio("According to the Hierarchy of Evidence, which of the following provides the highest level of primary evidence (Level 1)?",
                      ["Randomized Controlled Trial (RCT)", "Meta-Analysis", "Cohort Study", "Systematic Review"], 
                      index=None)

        st.subheader("Question 5")
        q5 = st.radio("A nursing committee wants to look backward in time to see if a rare adverse reaction is linked to a specific past medication. Which study design is best for looking backward at patient histories?",
                      ["Case-Control Study", "Cross-Sectional Survey", "Prospective Cohort Study", "Case Report"], 
                      index=None)

        submitted = st.form_submit_button("Submit Answers")

    # Updated Grading Logic (out of 5)
    if submitted:
        score = 0
        if q1 == "Comparison": score += 1
        if q2 == "Randomized Controlled Trial (RCT)": score += 1
        if q3 == "Cohort Study": score += 1
        if q4 == "Meta-Analysis": score += 1
        if q5 == "Case-Control Study": score += 1

        st.divider()
        st.subheader(f"Your Score: {score} / 5")

        if score == 5:
            st.balloons()
            st.success("🌟 Perfect score! You have mastered the Week 1 foundations.")
        elif score >= 3:
            st.info("👍 Great job! You have a solid grasp, but review the Study Design Hierarchy to brush up on a few details.")
        else:
            st.warning("📚 Keep practicing! Re-read Part 1 to solidify these core evidence-based practice concepts.")

def run():
    st.title("Week 1: Foundations of Study Design & Literature Search")
    
    tab1, tab2, tab3 = st.tabs(["Part 1: Study Materials", "Part 2: Interactive Sandbox", "Part 3: Knowledge Check"])
    
    with tab1:
        render_part_1()
        
    with tab2:
        render_part_2()
        
    with tab3:
        render_part_3()
