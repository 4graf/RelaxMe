"""
Модуль предоставляет API-маршруты для управления поставщиками.
"""

from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from lampu.api.dependencies import get_suppliers_service
from lampu.api.dependencies_user import validate_token
from lampu.helpers.error_codes import SupplierErrorCodes, AuthorizationErrorCodes
from lampu.models.users import Roles
from lampu.schemas.suppliers.supplier_exceptions import SupplierNotFoundException
from lampu.schemas.suppliers.supplier_info import SupplierInfo
from lampu.schemas.users.user_role import UserRole
from lampu.services.suppliers_service import SuppliersService

router = APIRouter()


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_suppliers(suppliers_service: Annotated[SuppliersService, Depends(get_suppliers_service)],
                            current_user: UserRole = Depends(validate_token)) -> List[SupplierInfo]:
    """
    Получает информацию о всех поставщиках.

        :param suppliers_service: Сервис для работы с поставщиками.
        :param current_user: Роль текущего пользователя
        :return: Список с информацией о поставщиках.
    """
    if current_user.role != Roles.ADMIN.value:
        error_code = AuthorizationErrorCodes.FORBIDDEN.value
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail={"code": error_code, "message": "List of suppliers allowed for admins only"})
    return await suppliers_service.get_suppliers()


@router.get("/{supplier_id}", status_code=status.HTTP_200_OK)
async def get_supplier(supplier_id: UUID,
                       suppliers_service: Annotated[SuppliersService, Depends(get_suppliers_service)],
                       current_user: UserRole = Depends(validate_token)) -> SupplierInfo:
    """
    Получает информацию о поставщике по его идентификатору.

        :param supplier_id: Идентификатор поставщика.
        :param suppliers_service: Сервис для работы с поставщиками.
        :param current_user: Роль текущего пользователя
        :return: Информация о поставщике.
    """

    try:
        return await suppliers_service.get_supplier_by_id(supplier_id=supplier_id)
    except SupplierNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"code": exc.code, "message": f"Supplier not found: {str(exc)}"}) from exc
