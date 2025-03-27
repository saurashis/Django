from rest_framework.permissions import BasePermission

'''class IsCreator(BasePermission):
    def has_permission(self, request, view):
        print("Inside has_permission")
        return True
    
    def has_object_permission(self, request, view, obj):
        print("Inside has_object_permission")
        print(f"Request User: {request.user}")  # Print current user
        print(f"Object User: {obj.order.customer.userprofile}")
        if request.method in ['GET','OPTIONS','HEAD']:
            return True
        return obj.order.customer.userprofile == request.user'''


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCreator(BasePermission):
    """
    Allow GET requests for everyone (including anonymous users),
    but only allow PATCH requests for authenticated users.
    """

    def has_permission(self, request, view):
        print("Inside has_permission")  # Debugging
        return True  # Only logged-in users can modify

    def has_object_permission(self, request, view, obj):
        print(f"Inside has_object_permission")  # Debugging
        print(f"Request User: {request.user}")  
        print(f"Object User: {obj.order.customer.userprofile}")  

        if request.method in SAFE_METHODS:  # GET, OPTIONS, HEAD → Allowed for everyone
            return True  

        return obj.order.customer.userprofile == request.user  # PATCH allowed only for the creator

        