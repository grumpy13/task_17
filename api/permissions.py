from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	mesaage = 'You are not the owner of this restaurant!'
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or request.user == obj.owner :
			return True
		return False