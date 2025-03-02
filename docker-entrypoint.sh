#!/bin/sh

# 确保目录存在并有正确的权限
mkdir -p /myblog/instance
chown -R www-data:www-data /myblog/instance
chmod 755 /myblog/instance

# 初始化数据库迁移（如果不存在）
if [ ! -d "migrations" ]; then
    echo "Initializing database migrations..."
    flask db init
fi

# 生成迁移文件
echo "Generating migration..."
flask db migrate -m "Initial migration"

# 应用迁移
echo "Applying migration..."
flask db upgrade

# 创建管理员账号（自动模式）
echo "Creating admin account..."
flask create-admin --auto

# 初始化测试数据（可选）
# flask init-data

# 启动应用
echo "Starting Flask application..."
python run.py 