from db_manager import DatabaseManager

manager = DatabaseManager('mysql+pymysql://root:example@localhost/tienda_db')

menu = \
'''
    1.- Listar Categorias
    2.- Insertar Categoria
    3.- Muestra Categoria por id
    4.- Actualizar Categoría
    5.- Eliminar Categoría
    6.- Salir
'''

def insert_category():
    category = input('Ingresa Categoría: ')
    description = input('Ingresa Descripción: ')
    sql = 'INSERT INTO categories(category, description) VALUES(:category, :description)'
    val = {'category': category, 'description': description}
    manager.execute_query(sql, val)

def list_categories():
    sql = 'SELECT * FROM categories'
    categories = manager.fetch_all(sql)
    for cat in categories:
        print(cat)

def get_category_by_id(id=None):
    if id == None:
        id = int(input('Ingresa el id de la Categoría a buscar: '))
    sql = 'SELECT * FROM categories WHERE id = :id'
    val = { 'id': id }
    cat = manager.fetch_one(sql, val)
    if cat is None:
        print('La Categoría no Existe')
    return cat

def delete_category():
    id = int(input('Ingresa el id de la Categoría a Eliminar: '))
    category = get_category_by_id(id)
    if category is None: 
        return
    confirm = input('Quiere eliminar la categoría? S/N: ')
    if confirm == 'S':
        sql = 'DELETE FROM categories WHERE id = :id'
        val = {'id': id}
        manager.execute_query(sql, val)

def update_category():
    id = int(input('Ingresa el id de la Categoría a Actualizar: '))
    category = get_category_by_id(id)
    if category is None:
        return
    category_cat = input('Ingresa nueva: ')
    if category_cat == '':
        category_cat = category['category']
    category_desc = input('Ingresa la nueva descripción: ')
    if category_desc == '':
        category_desc = category['description']
    
    sql = "UPDATE categories SET category = :category, description = :description WHERE id = :id"
    val = {'category': category_cat, 'description': category_desc, 'id': id}
    manager.execute_query(sql, val)
    print(get_category_by_id(id))
    print('Categoría Actualizada')

while True:
    option = input(menu)
    match(option):
        case '1':
            list_categories()
        case '2':
            insert_category()
        case '3':
            get_category_by_id()
        case '4':
            update_category()
        case '5':
            delete_category()
        case '6':
            print('Bye!')
            break
        case _:
            print('Opción no válida')