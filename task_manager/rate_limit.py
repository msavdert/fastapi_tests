from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request
from config import settings

# Create a limiter instance
limiter = Limiter(key_func=get_remote_address)

# Configure rate limits
# 5 requests per minute for authentication endpoints
auth_limiter = limiter.limit(f"{settings.AUTH_RATE_LIMIT_PER_MINUTE}/minute")

# 30 requests per minute for task endpoints
task_limiter = limiter.limit(f"{settings.RATE_LIMIT_PER_MINUTE}/minute")

# 100 requests per minute for general endpoints
general_limiter = limiter.limit(f"{settings.RATE_LIMIT_PER_MINUTE}/minute") 