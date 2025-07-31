from apps.web.models import Instructor


def instructor_name_to_id():
    """
    Returns a dictionary mapping instructor names to their database IDs.
    """
    return {
        instructor.name: instructor.id 
        for instructor in Instructor.objects.all()
    }


def get_instructor_id(instructor_name):
    """
    Returns the database ID for a given instructor name, or None if not found.
    """
    try:
        return Instructor.objects.get(name=instructor_name).id
    except Instructor.DoesNotExist:
        return None


def get_instructor_name(instructor_id):
    """
    Returns the name for a given instructor ID, or None if not found.
    """
    try:
        return Instructor.objects.get(id=instructor_id).name
    except Instructor.DoesNotExist:
        return None


def get_all_instructors():
    """
    Returns all instructors as a list of dictionaries with 'id' and 'name' keys.
    """
    return [
        {'id': instructor.id, 'name': instructor.name}
        for instructor in Instructor.objects.all().order_by('name')
    ]


def get_all_instructor_names():
    """
    Returns a list of all instructor names, sorted alphabetically.
    """
    return list(Instructor.objects.values_list('name', flat=True).order_by('name'))


def get_all_instructor_ids():
    """
    Returns a list of all instructor IDs.
    """
    return list(Instructor.objects.values_list('id', flat=True))
