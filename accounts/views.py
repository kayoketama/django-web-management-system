from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ContactMessage


@login_required
def profile(request):
    return render(
        request,
        "accounts/profile.html"
    )


@login_required
def dashboard(request):
    total_users = User.objects.count()
    total_messages = ContactMessage.objects.count()

    context = {
        "total_users": total_users,
        "total_messages": total_messages,
    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )


@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    total_users = User.objects.count()
    total_messages = ContactMessage.objects.count()

    context = {
        "total_users": total_users,
        "total_messages": total_messages,
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context
    )
    
    
@login_required
def admin_users(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    search = request.GET.get("search", "")

    users = User.objects.all()

    if search:
        users = users.filter(
            username__icontains=search
        ) | users.filter(
            email__icontains=search
        )

    context = {
        "users": users,
        "search": search,
    }

    return render(
        request,
        "accounts/admin_users.html",
        context
    )
@login_required
def admin_user_detail(request, user_id):

    if not request.user.is_staff:
        return redirect("dashboard")

    user = User.objects.get(id=user_id)

    context = {
        "user_detail": user,
    }

    return render(
        request,
        "accounts/admin_user_detail.html",
        context
    )
@login_required
def admin_user_delete(request, user_id):

    if not request.user.is_staff:
        return redirect("dashboard")

    user = User.objects.get(id=user_id)

    if user.id == request.user.id:
        messages.error(
            request,
            "You cannot delete your own account."
        )
        return redirect("admin_users")

    if request.method == "POST":
        user.delete()

        messages.success(
            request,
            "User deleted successfully."
        )

        return redirect("admin_users")

    return render(
        request,
        "accounts/admin_user_delete.html",
        {"user_detail": user}
    )
@login_required
def admin_messages(request):

    if not request.user.is_staff:
        return redirect("dashboard")

    search = request.GET.get("search", "")

    messages_list = ContactMessage.objects.all().order_by("-created_at")

    if search:
        messages_list = messages_list.filter(
            name__icontains=search
        ) | messages_list.filter(
            email__icontains=search
        )

    context = {
        "messages_list": messages_list,
        "search": search,
    }

    return render(
        request,
        "accounts/admin_messages.html",
        context
    )
@login_required
def admin_message_delete(request, message_id):

    if not request.user.is_staff:
        return redirect("dashboard")

    message = ContactMessage.objects.get(id=message_id)

    if request.method == "POST":
        message.delete()

        messages.success(
            request,
            "Message deleted successfully."
        )

        return redirect("admin_messages")

    return render(
        request,
        "accounts/admin_message_delete.html",
        {"message": message}
    )
@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user

        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        # Check username uniqueness
        if User.objects.filter(username=username).exclude(
            id=user.id
        ).exists():
            messages.error(
                request,
                "This username is already taken."
            )

            return redirect("edit_profile")

        # Update user information
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        user.save()

        messages.success(
            request,
            "Profile updated successfully!"
        )

        return redirect("edit_profile")

    return render(
        request,
        "accounts/edit_profile.html"
    )


@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not request.user.check_password(current_password):
            messages.error(
                request,
                "Current password is incorrect."
            )

            return render(
                request,
                "accounts/change_password.html"
            )

        if len(new_password) < 8:
            messages.error(
                request,
                "New password must be at least 8 characters."
            )

            return render(
                request,
                "accounts/change_password.html"
            )

        if new_password != confirm_password:
            messages.error(
                request,
                "New passwords do not match."
            )

            return render(
                request,
                "accounts/change_password.html"
            )

        request.user.set_password(new_password)
        request.user.save()

        messages.success(
            request,
            "Password changed successfully."
        )

        return redirect("change_password")

    return render(
        request,
        "accounts/change_password.html"
    )


def home(request):
    return render(
        request,
        "accounts/home.html"
    )


def about(request):
    return render(
        request,
        "accounts/about.html"
    )


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(
            request,
            "Message sent successfully!"
        )

        return redirect("contact")

    return render(
        request,
        "accounts/contact.html"
    )