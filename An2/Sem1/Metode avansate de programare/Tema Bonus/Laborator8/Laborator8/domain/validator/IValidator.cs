
namespace Laborator8.domain.validator
{
    public interface IValidator<E>
    {
        void Validate(E e);
    }
}
