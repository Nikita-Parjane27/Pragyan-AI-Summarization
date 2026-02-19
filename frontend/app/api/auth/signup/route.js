import { supabase } from "@/lib/supabase";

export async function POST(req) {
  try {
    const { name, email, password } = await req.json();

    if (!email || !password) {
      return Response.json(
        { success: false, message: "Email and password are required" },
        { status: 400 }
      );
    }

    const { data, error } = await supabase.auth.signUp({
      email: email,
      password: password,
      options: {
        data: { full_name: name }
      }
    });

    if (error) {
      return Response.json(
        { success: false, message: error.message },
        { status: 400 }
      );
    }

    return Response.json({
      success: true,
      message: "Account created! Please check your email to verify.",
      user: data.user,
    });

  } catch (err) {
    console.error("Signup Error:", err);
    return Response.json(
      { success: false, message: "Internal server error" },
      { status: 500 }
    );
  }
}