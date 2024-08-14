from typing import Optional

from fastapi_pa

class AddressFilter(Filter):
    street: Optional[str]
    country: Optional[str]
    city__in: Optional[list[str]]

    class Constants(Filter.Constants):
        model = Address


class UserFilter(Filter):
    name: Optional[str]
    address: Optional[AddressFilter] = FilterDepends(with_prefix("address", AddressFilter))

    class Constants(Filter.Constants):
        model = User


@app.get("/users", response_model=list[UserOut])
async def get_users(user_filter: UserFilter = FilterDepends(UserFilter), db: AsyncSession = Depends(get_db)) -> Any:
    query = user_filter.filter(select(User).outerjoin(Address))   #
    result = await db.execute(query)

    return result.scalars().all()

