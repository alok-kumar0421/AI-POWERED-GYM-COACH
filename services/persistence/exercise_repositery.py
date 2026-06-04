from services.persistence.supabase_client import supabase


def init_db():
    pass


def get_user(username):
    result = (
        supabase.table("users")
        .select("*")
        .eq("username", username)
        .execute()
    )

    return result.data[0] if result.data else None


def create_user(username):
    supabase.table("users").insert({
        "username": username
    }).execute()

    return get_user(username)


def get_or_create_user(username):
    user = get_user(username)

    if user is None:
        user = create_user(username)

    return user


def add_exercise(user_id, exercise_name, reps, sets, time):

    existing = (
        supabase.table("exercises")
        .select("*")
        .eq("user_id", user_id)
        .eq("exercise_name", exercise_name)
        .execute()
    )

    if existing.data:
        row = existing.data[0]

        supabase.table("exercises").update({
            "reps": row["reps"] + reps,
            "sets": row["sets"] + sets,
            "time": row["time"] + time
        }).eq("id", row["id"]).execute()

    else:
        supabase.table("exercises").insert({
            "user_id": user_id,
            "exercise_name": exercise_name,
            "reps": reps,
            "sets": sets,
            "time": time
        }).execute()


def get_users_exercises(user_id):

    result = (
        supabase.table("exercises")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return result.data