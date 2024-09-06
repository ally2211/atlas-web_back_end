## Pagination

### 1. **Paginate a Dataset with Simple `page` and `page_size` Parameters**

Paginating a dataset with `page` and `page_size` allows you to divide the dataset into manageable chunks for display purposes. Here's how to do it:

#### Formula for Pagination:
- **`page`**: The current page number (starting from 1).
- **`page_size`**: The number of items per page.

The formula to calculate the slice of data for each page:

```python
start_index = (page - 1) * page_size
end_index = start_index + page_size
```

Using this, you can slice your dataset like this:

```python
def paginate(data, page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return data[start_index:end_index]

# Example
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
page = 2
page_size = 3
print(paginate(data, page, page_size))  # Output: [4, 5, 6]
```

This returns the portion of the dataset corresponding to the current page.

### 2. **Paginate a Dataset with Hypermedia Metadata**

Hypermedia pagination adds metadata to the paginated response, making it easier to navigate between pages. This includes details such as:

- `total_items`: Total number of items in the dataset.
- `total_pages`: Total number of pages.
- `current_page`: The current page number.
- `next_page`: Link or indication of the next page (if applicable).
- `prev_page`: Link or indication of the previous page (if applicable).

Here's an example:

```python
def paginate_with_metadata(data, page, page_size):
    total_items = len(data)
    total_pages = (total_items + page_size - 1) // page_size  # Round up
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_data = data[start_index:end_index]

    metadata = {
        'total_items': total_items,
        'total_pages': total_pages,
        'current_page': page,
        'next_page': page + 1 if page < total_pages else None,
        'prev_page': page - 1 if page > 1 else None
    }

    return {
        'data': paginated_data,
        'metadata': metadata
    }

# Example
data = list(range(1, 51))  # A dataset of 50 items
result = paginate_with_metadata(data, 2, 10)
print(result)
```

This returns both the data and the metadata that helps the client navigate through the pages.

### 3. **Paginate in a Deletion-Resilient Manner**

When items can be deleted from the dataset, using fixed indices based on `page` and `page_size` might break consistency, especially if an item is deleted and pages shift.

To handle this in a deletion-resilient way, you can use **cursors** or **unique identifiers** (e.g., database IDs) for pagination, rather than relying on fixed indices.

#### Cursor-Based Pagination:

Instead of passing the `page` number, pass a **cursor** that indicates the starting point (e.g., the unique identifier of the last item from the previous page). For each request, you fetch items starting after the given cursor.

```python
def paginate_with_cursor(data, cursor, page_size):
    # Sort by unique id (assumes `data` is a list of dictionaries with `id`)
    data_sorted = sorted(data, key=lambda x: x['id'])
    
    # Find the index of the cursor in the sorted data
    if cursor is not None:
        start_index = next((i for i, item in enumerate(data_sorted) if item['id'] > cursor), 0)
    else:
        start_index = 0  # If no cursor, start from the beginning

    paginated_data = data_sorted[start_index:start_index + page_size]
    
    # The next cursor is the id of the last item in the current page
    next_cursor = paginated_data[-1]['id'] if len(paginated_data) == page_size else None

    return {
        'data': paginated_data,
        'next_cursor': next_cursor
    }

# Example
data = [{'id': i, 'value': f'item {i}'} for i in range(1, 21)]  # A dataset with unique ids
cursor = 5  # Let's assume we are starting after id 5
result = paginate_with_cursor(data, cursor, 5)
print(result)
```

This approach is **resilient to deletions**, as it relies on the `id` of the items rather than their index in a shifting array. Even if an item is deleted, the next cursor points to the next valid item.

## Task 0:  Simple Helper Function
Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

A **tuple** is a fundamental data structure in Python that is used to store multiple items in a single variable. It is similar to a list, but with a key distinction: **tuples are immutable**, meaning that once a tuple is created, its contents cannot be changed (i.e., you cannot modify, add, or remove elements). Tuples are often used to group together related data that shouldn’t change.

### Key Characteristics of Tuples:
1. **Ordered**: The elements in a tuple have a defined order and can be accessed by their index.
2. **Immutable**: Once a tuple is created, you cannot modify its elements.
3. **Allows Duplicates**: Like lists, tuples can contain duplicate elements.
4. **Indexed**: You can access tuple elements using their index, starting at 0.

### Creating Tuples:
Tuples are defined by enclosing elements in parentheses `()`, separated by commas.

```python
# Example of a tuple
my_tuple = (1, 2, 3)

# A tuple with mixed data types
mixed_tuple = ("apple", 10, True)

# A tuple can also contain other tuples (nested tuple)
nested_tuple = (1, (2, 3), (4, 5))
```

### Accessing Elements in a Tuple:
You can access elements in a tuple using indexing or slicing.

```python
# Accessing by index
my_tuple = (10, 20, 30)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30

# Slicing a tuple
print(my_tuple[1:3])  # Output: (20, 30)
```

### Tuples with One Element:
To create a tuple with a single element, you need to include a comma after the element. This is because parentheses alone don’t define a tuple; the comma is what makes it a tuple.

```python
# Single element tuple
single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
```

### Immutability of Tuples:
Once a tuple is created, you cannot change, add, or remove elements.

```python
my_tuple = (1, 2, 3)

# This will raise an error as tuples are immutable
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

### Tuple Operations:

- **Concatenation**: You can concatenate two or more tuples.
  ```python
  tuple1 = (1, 2)
  tuple2 = (3, 4)
  result = tuple1 + tuple2
  print(result)  # Output: (1, 2, 3, 4)
  ```

- **Repetition**: You can repeat a tuple using the `*` operator.
  ```python
  my_tuple = (1, 2)
  print(my_tuple * 2)  # Output: (1, 2, 1, 2)
  ```

- **Membership**: You can check if an element is in a tuple using the `in` keyword.
  ```python
  my_tuple = (1, 2, 3)
  print(2 in my_tuple)  # Output: True
  ```

### Tuples vs Lists:
- **Mutability**: The primary difference between tuples and lists is that lists are mutable (you can change their content), whereas tuples are immutable.
- **Performance**: Tuples can be more efficient than lists in terms of memory usage and performance because of their immutability.
- **Use Case**: Use tuples when you need a collection of items that should not change. For example, fixed data like coordinates `(x, y)` or representing a point `(latitude, longitude)`.

### Practical Example:

Tuples are often used to return multiple values from a function, which is a common use case.

```python
# Function returning multiple values as a tuple
def get_coordinates():
    return (25.0, 75.5)

coordinates = get_coordinates()
print(coordinates)  # Output: (25.0, 75.5)
```

In this case, the tuple is used to group together related data (latitude and longitude) that should not change.

### Conclusion:
Tuples are a versatile and efficient data structure when you need to store ordered, unchangeable collections of items. They're widely used when the immutability of data is important, like in function return values or configuration settings that shouldn't be altered after initialization.

## Task 1:  Simple Pagination
Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should be returned.