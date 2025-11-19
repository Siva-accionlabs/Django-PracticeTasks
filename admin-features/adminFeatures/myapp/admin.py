from django.contrib import admin
from .models import Student, Course, Enrollment

# Register your models here.


# Inline Admin Example
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
    fields = ("course", "marks")
    readonly_fields = ("course",)


# Student Admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "gender",
        "grade",
        "is_active",
        "admission_date",
        "full_name",
    )

    # search
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "id",
    )

    # list_filter
    list_filter = ("gender", "grade", "is_active")

    # list_editable
    list_editable = (
        "grade",
        "is_active",
    )

    # ordering
    ordering = ("first_name",)

    # inlines
    inlines = [EnrollmentInline]

    # readonly
    readonly_fields = ("admission_date",)

    # custom function to display whatever we want to display based on list_display
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "Student Name"

    # fieldsets
    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "gender",
                    "date_of_birth",
                ),
            },
        ),
        ("Academic", {"fields": ("grade", "is_active")}),
        ("System Info", {"fields": ("admission_date",), "classes": ("collapse",)}),
    )

    # Enrollment Admin
    @admin.register(Enrollment)
    class EnrollmentAdmin(admin.ModelAdmin):
        list_display = ("id", "student", "course", "enrolled_on", "marks")
        list_filter = ("course", "enrolled_on")
        search_fields = ("student__first_name", "student__last_name", "course__name")
    
    
