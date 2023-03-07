using Laborator8.domain;

namespace Laborator8.domain.validator
{
    public class JucatorValidator : IValidator<Jucator>
    {
        public void Validate(Jucator jucator)
        {
            if (jucator.ID <= 0)
                throw new ValidationException("ID-ul nu poate fi mai mic sau egal cu 0");
            if (string.IsNullOrWhiteSpace(jucator.Nume))
                throw new ValidationException("Numele nu poate fi gol");
            if (jucator.Echipa == null)
                throw new ValidationException("Echipa nu poate fi null");
        }
    }
}