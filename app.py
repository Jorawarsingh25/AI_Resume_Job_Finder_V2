import streamlit as st
from resume_parser import extract_text
from job_fetcher import fetch_jobs
from matcher import get_match_score
from ats_score import calculate_ats_score
from missing_skills import get_missing_skills

st.set_page_config(
    page_title="AI Resume Job Finder",
    layout="wide"
)

st.title("🚀 AI Resume Job Finder")

resume = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if resume is not None:

    try:

        st.success("✅ Resume Uploaded Successfully!")

        # Resume Text
        resume_text = extract_text(resume)

        st.subheader("📄 Resume Text")

        st.text_area(
            "Extracted Resume Content",
            value=resume_text,
            height=250
        )

        # ATS Score
        ats_score, found_skills = calculate_ats_score(
            resume_text
        )

        st.subheader("📊 ATS Score")

        st.metric(
            label="ATS Score",
            value=f"{ats_score}%"
        )

        if ats_score >= 80:
            st.success("✅ Strong Resume")
        elif ats_score >= 60:
            st.warning("⚠️ Good Resume")
        else:
            st.error("❌ Resume Needs Improvement")

        # Skills Found
        st.subheader("✅ Skills Found")

        if found_skills:
            for skill in found_skills:
                st.write(f"✔ {skill}")
        else:
            st.warning("No skills detected.")

        # Missing Skills
        st.subheader("❌ Missing Skills")

        missing = get_missing_skills(resume_text)

        if len(missing) == 0:
            st.success("Great! No major skills missing.")
        else:
            for skill in missing:
                st.write(f"❌ {skill}")

        st.markdown("---")

        # Fetch Jobs
        st.subheader("🔍 Fetching Latest Jobs...")

        jobs = fetch_jobs()

        st.success(f"Jobs Found: {len(jobs)}")

        if jobs.empty:

            st.error("No jobs found.")

        else:

            scores = []

            for _, row in jobs.iterrows():

                score = get_match_score(
                    resume_text,
                    row["description"]
                )

                scores.append(score)

            jobs["Match Score"] = scores

            jobs = jobs.sort_values(
                by="Match Score",
                ascending=False
            )

            st.subheader("🎯 Best Matching Jobs")

            for _, row in jobs.iterrows():

                st.markdown(
                    f"### {row['title']}"
                )

                st.write(
                    f"🏢 Company: {row['company']}"
                )

                st.write(
                    f"📅 Posted: {row['posted_date']}"
                )

                st.write(
                    f"📊 Match Score: {row['Match Score']}%"
                )

                if row["apply_link"]:

                    st.link_button(
                        "🚀 Apply Now",
                        row["apply_link"]
                    )

                st.markdown("---")

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )