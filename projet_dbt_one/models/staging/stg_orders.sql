with source as (
    select * from {{ source('my_dbt_db', 'orders') }}
),
renamed as (
    select
        id as order_id,
        customer as customer_id,
        ordered_at as order_date,
        store_id as store_location_id
    from source
)
select * from renamed
