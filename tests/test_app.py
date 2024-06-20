def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john, jane, alice"

"""
Add a new user
"""
def test_adding_new_user(web_client):
    response = web_client.post('/users', data={
        'id': '4',
        'username': 'tina'
        })
    assert response.status_code == 201
    assert response.data.decode("utf-8") == "User tina created with id 4"


"""
Update username
"""
def test_updating_username(web_client):
    response = web_client.put('/users/3', data={'username': 'anna'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Id 3 updated with username anna"

"""
Given a speciic user id of 1
This user is deleted from our list of dictionaries
"""
def test_deleting_user(web_client):
    response = web_client.delete('/users/1')
    assert response.data.decode("utf-8") == "Message: User deleted"

"""
Given no username
when trying to create a new user:
return error message "Error: Username is required", 400
"""
def test_create_new_user_without_username(web_client):
    response = web_client.post('/users', data={
        'id': '4' 
        })
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "Error: Username is required"
