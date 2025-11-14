    # ---------------- GAME BOARD ----------------
    if "players" in st.session_state:

        st.subheader(f"Turn: {st.session_state['turn']} ({st.session_state['players'][st.session_state['turn']]})")

        # Restart button
        if st.button("Restart Game"):
            st.session_state["board"] = [""] * 9
            st.session_state["turn"] = "X"
            st.experimental_rerun()

        cols = st.columns(3)
        for i in range(9):
            if cols[i % 3].button(st.session_state["board"][i] or " ", key=f"cell_{i}"):
                if st.session_state["board"][i] == "":
                    st.session_state["board"][i] = st.session_state["turn"]
                    winner = check_winner(st.session_state["board"])

                    if winner:
                        winner_name = st.session_state["players"][winner]

                        st.success(f"{winner_name} wins!")

                        # Store in DB
                        tournament_collection.insert_one({
                            "winner": winner_name,
                            "symbol": winner
                        })

                        st.balloons()
                        return

                    # Switch turn
                    st.session_state["turn"] = "O" if st.session_state["turn"] == "X" else "X"
                    st.experimental_rerun()
